"""Pluggable secret resolution.

A secret *reference* is a string with an optional scheme:

===================  ===========================================================
``env:NAME``         Read from the process environment (Kubernetes ``env``)
``file:/path``       Read from a file (Kubernetes Secret volume, Docker secret)
``k8s:NAME``         Read ``<secretsFileDir>/NAME`` (projected Secret volume)
``enc:<token>``      Fernet ciphertext stored inside MongoDB
``vault:path#key``   External secret manager (pluggable provider)
``<literal>``        Literal value - permitted only in non-production envs
===================  ===========================================================

Nothing here ever logs a resolved value.
"""

from __future__ import annotations

import os
from abc import ABC, abstractmethod
from collections.abc import Mapping
from pathlib import Path
from typing import Any

from reconx.common.errors import SecretResolutionError
from reconx.common.logging import get_logger
from reconx.config.settings import Settings, get_settings
from reconx.security import crypto

log = get_logger(__name__)


class SecretProvider(ABC):
    """A backend able to resolve one scheme of secret reference."""

    scheme: str = ""

    @abstractmethod
    def resolve(self, reference: str) -> str: ...

    def available(self) -> bool:  # pragma: no cover - trivial default
        return True


class EnvSecretProvider(SecretProvider):
    scheme = "env"

    def resolve(self, reference: str) -> str:
        value = os.getenv(reference)
        if value is None:
            raise SecretResolutionError(f"Environment variable '{reference}' is not set")
        return value


class FileSecretProvider(SecretProvider):
    scheme = "file"

    def resolve(self, reference: str) -> str:
        path = Path(reference)
        if not path.is_file():
            raise SecretResolutionError(f"Secret file '{reference}' does not exist")
        return path.read_text(encoding="utf-8").strip()


class KubernetesSecretProvider(SecretProvider):
    """Reads keys from a projected Secret volume (``/var/run/secrets/reconx``)."""

    scheme = "k8s"

    def __init__(self, base_dir: str) -> None:
        self.base_dir = Path(base_dir)

    def resolve(self, reference: str) -> str:
        path = self.base_dir / reference
        if not path.is_file():
            raise SecretResolutionError(
                f"Kubernetes secret key '{reference}' not found under {self.base_dir}"
            )
        return path.read_text(encoding="utf-8").strip()


class EncryptedSecretProvider(SecretProvider):
    scheme = "enc"

    def __init__(self, key: str | None = None) -> None:
        self.key = key

    def resolve(self, reference: str) -> str:
        return crypto.decrypt(f"{crypto.ENC_PREFIX}{reference}", self.key)


class VaultSecretProvider(SecretProvider):
    """External secret manager hook.

    Ships with an HTTP KV-v2 client shape but stays inert unless
    ``VAULT_ADDR``/``VAULT_TOKEN`` are configured, so the platform never
    hard-depends on Vault being present.
    """

    scheme = "vault"

    def available(self) -> bool:
        return bool(os.getenv("VAULT_ADDR") and os.getenv("VAULT_TOKEN"))

    def resolve(self, reference: str) -> str:
        if not self.available():
            raise SecretResolutionError(
                "vault: secret reference used but VAULT_ADDR/VAULT_TOKEN are not configured"
            )
        import json
        import urllib.request

        path, _, key = reference.partition("#")
        addr = os.environ["VAULT_ADDR"].rstrip("/")
        if not addr.startswith(("http://", "https://")):
            raise SecretResolutionError(
                "VAULT_ADDR must be an http(s) URL", details={"scheme": addr.split(':', 1)[0]}
            )
        mount = os.getenv("VAULT_KV_MOUNT", "secret")
        url = f"{addr}/v1/{mount}/data/{path.lstrip('/')}"
        # The scheme is asserted above, so this can only ever be an HTTP(S) call.
        request = urllib.request.Request(url, headers={"X-Vault-Token": os.environ["VAULT_TOKEN"]})  # noqa: S310
        try:
            with urllib.request.urlopen(request, timeout=10) as response:  # noqa: S310
                payload = json.loads(response.read().decode())
        except Exception as exc:
            raise SecretResolutionError(f"Vault lookup failed for '{path}'") from exc
        data = payload.get("data", {}).get("data", {})
        if key:
            if key not in data:
                raise SecretResolutionError(f"Vault path '{path}' has no key '{key}'")
            return str(data[key])
        if len(data) == 1:
            return str(next(iter(data.values())))
        raise SecretResolutionError(f"Vault path '{path}' holds multiple keys; use 'vault:{path}#key'")


class SecretResolver:
    """Resolves secret references using the configured providers."""

    def __init__(self, settings: Settings | None = None) -> None:
        self.settings = settings or get_settings()
        sec = self.settings.security
        self.providers: dict[str, SecretProvider] = {
            "env": EnvSecretProvider(),
            "file": FileSecretProvider(),
            "k8s": KubernetesSecretProvider(sec.secrets_file_dir),
            "enc": EncryptedSecretProvider(sec.encryption_key),
            "vault": VaultSecretProvider(),
        }
        self.allow_literals = self.settings.environment.lower() in {"local", "dev", "development", "test"}

    def register(self, provider: SecretProvider) -> None:
        self.providers[provider.scheme] = provider

    def resolve(self, reference: str | None, *, field: str = "secret") -> str | None:
        if reference is None or reference == "":
            return None
        scheme, sep, rest = str(reference).partition(":")
        if sep and scheme in self.providers:
            try:
                return self.providers[scheme].resolve(rest)
            except SecretResolutionError:
                raise
            except Exception as exc:
                raise SecretResolutionError(f"Could not resolve {scheme}: secret for '{field}'") from exc
        if not self.allow_literals:
            log.warning(
                "secrets.literal_value_used",
                field=field,
                environment=self.settings.environment,
                hint="Use env:/file:/k8s:/enc:/vault: references outside development",
            )
        return str(reference)

    def resolve_mapping(self, config: Mapping[str, Any], secret_fields: frozenset[str]) -> dict[str, Any]:
        """Return a copy of ``config`` with secret fields resolved to plain values."""
        resolved: dict[str, Any] = {}
        for key, value in config.items():
            if key in secret_fields and isinstance(value, str) and value:
                resolved[key] = self.resolve(value, field=key)
            else:
                resolved[key] = value
        return resolved

    def encrypt_for_storage(self, value: str) -> str:
        """Encrypt a UI-entered plaintext secret so MongoDB never sees it raw."""
        if any(str(value).startswith(f"{scheme}:") for scheme in self.providers):
            return value  # already a reference
        return crypto.encrypt(value, self.settings.security.encryption_key)


_default_resolver: SecretResolver | None = None


def get_secret_resolver(settings: Settings | None = None) -> SecretResolver:
    global _default_resolver
    if _default_resolver is None or settings is not None:
        _default_resolver = SecretResolver(settings)
    return _default_resolver
