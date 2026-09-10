# ReconX - developer workflow
#
#   make help          list every target
#   make install       create .venv and install the project with dev extras
#   make test          run the whole test suite
#   make docker-up     bring up the local stack (UI on :8501, API on :8000)

SHELL := /bin/bash
.DEFAULT_GOAL := help

PYTHON      ?= python3.11
VENV        ?= .venv
BIN         := $(VENV)/bin
PYTEST      := $(BIN)/pytest
RUFF        := $(BIN)/ruff
MYPY        := $(BIN)/mypy
COMPOSE     ?= docker compose
IMAGE_TAG   ?= 1.0.0
REGISTRY    ?=
HELM_RELEASE?= reconx
NAMESPACE   ?= reconx

export PYTHONPATH := src

## ----------------------------------------------------------------- help
.PHONY: help
help: ## Show this help
	@echo "ReconX $(IMAGE_TAG) - available targets:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) \
	  | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-22s\033[0m %s\n", $$1, $$2}'

## --------------------------------------------------------------- setup
.PHONY: install
install: ## Create the virtualenv and install the project (all extras + dev)
	$(PYTHON) -m venv $(VENV)
	$(BIN)/pip install --upgrade pip setuptools wheel
	$(BIN)/pip install -e ".[api,ui,spark,connectors,dev]"
	@echo "Done. Activate with: source $(BIN)/activate"

.PHONY: jars
jars: ## Download the JDBC drivers Spark needs
	./scripts/fetch-jdbc-drivers.sh deployment/docker/jars
	./scripts/fetch-jdbc-drivers.sh .jars

.PHONY: build
build: ## Build the wheel and source distribution
	$(BIN)/pip install --upgrade build
	$(BIN)/python -m build

## ---------------------------------------------------------------- quality
.PHONY: lint
lint: ## Run ruff and the driver-materialisation guard
	$(RUFF) check src tests
	./scripts/check_no_unbounded_collect.sh

.PHONY: hooks
hooks: ## Install the pre-commit hooks
	$(BIN)/pre-commit install

.PHONY: format
format: ## Format with ruff
	$(RUFF) format src tests
	$(RUFF) check --fix src tests

.PHONY: typecheck
typecheck: ## Run mypy over the source tree
	$(MYPY) src/reconx

.PHONY: validate-config
validate-config: ## Validate the example reconciliation and the Helm chart
	$(BIN)/python -m reconx.cli validate examples/sample-reconciliation.yaml
	$(BIN)/python -m reconx.cli validate examples/local-demo.yaml
	$(BIN)/python scripts/validate_helm_chart.py

## ------------------------------------------------------------------ test
.PHONY: test
test: ## Run the whole test suite
	$(PYTEST) tests -q

.PHONY: test-unit
test-unit: ## Fast tests only (no Spark, no external services)
	$(PYTEST) tests/unit -q -m "not spark"

.PHONY: test-spark
test-spark: ## Tests that start a local SparkSession
	$(PYTEST) tests -q -m spark

.PHONY: test-integration
test-integration: ## Repository and API tests
	$(PYTEST) tests/integration -q

.PHONY: test-e2e
test-e2e: ## Full pipeline test
	$(PYTEST) tests/e2e -q

.PHONY: coverage
coverage: ## Test suite with a coverage report
	$(PYTEST) tests --cov=reconx --cov-report=term-missing --cov-report=html
	@echo "HTML report: htmlcov/index.html"

.PHONY: check
check: lint typecheck test validate-config ## Everything CI runs

## -------------------------------------------------------------- run local
.PHONY: run-api
run-api: ## Run the API (http://localhost:8000/docs)
	$(BIN)/uvicorn reconx.api.main:app --reload --host 0.0.0.0 --port 8000

.PHONY: run-ui
run-ui: ## Run the Streamlit UI (http://localhost:8501)
	$(BIN)/streamlit run src/reconx/ui/streamlit_app.py --server.port 8501

.PHONY: run-scheduler
run-scheduler: ## Run the scheduler loop
	$(BIN)/python -m reconx.scheduler.service

.PHONY: run
run: docker-up ## Alias for docker-up

.PHONY: demo
demo: ## Run the self-contained demo reconciliation (no external services)
	RESULT_SQLALCHEMY_URL="sqlite:///$(PWD)/.data/demo-metrics.db" \
	KAFKA_ENABLED=false SPARK_MASTER="local[*]" LOG_FORMAT=console \
	$(BIN)/python -m reconx.spark.job \
	  --definition-file examples/local-demo.yaml \
	  --connections-file examples/local-demo-connections.yaml \
	  --business-date 2026-09-10 \
	  --param data_dir=$(PWD)/examples/data --param out_dir=$(PWD)/.data/demo-output \
	  --profile --no-notifications

## ---------------------------------------------------------------- docker
.PHONY: docker-build
docker-build: ## Build every container image
	$(COMPOSE) build

.PHONY: docker-up
docker-up: ## Start the local stack
	$(COMPOSE) up -d
	@echo ""
	@echo "  UI          http://localhost:8501   (admin / reconx-admin)"
	@echo "  API docs    http://localhost:8000/docs"
	@echo "  Kafka UI    http://localhost:8080"
	@echo "  MinIO       http://localhost:9001   (reconx / reconx-secret)"
	@echo "  Mailpit     http://localhost:8025"
	@echo "  Spark       http://localhost:8090"

.PHONY: docker-down
docker-down: ## Stop the local stack
	$(COMPOSE) down

.PHONY: docker-clean
docker-clean: ## Stop the stack and delete its volumes
	$(COMPOSE) down -v

.PHONY: docker-logs
docker-logs: ## Tail the stack logs
	$(COMPOSE) logs -f --tail=100

.PHONY: docker-push
docker-push: ## Push the images to $(REGISTRY)
	@test -n "$(REGISTRY)" || (echo "Set REGISTRY=registry.example.com/" && exit 1)
	for image in api ui scheduler spark; do \
	  docker tag reconx/$$image:$(IMAGE_TAG) $(REGISTRY)reconx/$$image:$(IMAGE_TAG); \
	  docker push $(REGISTRY)reconx/$$image:$(IMAGE_TAG); \
	done

## ------------------------------------------------------------ kubernetes
.PHONY: k8s-apply
k8s-apply: ## Apply the raw Kubernetes manifests
	kubectl apply -f deployment/kubernetes/

.PHONY: k8s-validate
k8s-validate: ## Server-side dry run of the manifests
	kubectl apply --dry-run=server -f deployment/kubernetes/

.PHONY: helm-lint
helm-lint: ## Lint the Helm chart
	helm lint deployment/helm/reconx
	$(BIN)/python scripts/validate_helm_chart.py

.PHONY: helm-template
helm-template: ## Render the chart locally
	helm template $(HELM_RELEASE) deployment/helm/reconx --namespace $(NAMESPACE)

.PHONY: helm-install
helm-install: ## Install/upgrade the chart
	helm upgrade --install $(HELM_RELEASE) deployment/helm/reconx \
	  --namespace $(NAMESPACE) --create-namespace \
	  --set security.encryptionKey="$$(reconx-admin gen-key)"

## ------------------------------------------------------------- database
.PHONY: db-ddl
db-ddl: ## Regenerate the SQL migration from the SQLAlchemy models
	$(BIN)/python -c "from sqlalchemy.schema import CreateTable, CreateIndex; \
	from sqlalchemy.dialects import postgresql; \
	from reconx.metrics.models import ALL_TABLES; \
	out = ['-- ReconX metrics database schema (PostgreSQL)', '-- Generated from reconx.metrics.models - regenerate with \`make db-ddl\`.', '-- Apply with: psql -f V1__initial_schema.sql', '']; \
	[out.extend([str(CreateTable(t, if_not_exists=True).compile(dialect=postgresql.dialect())).strip() + ';', ''] + [str(CreateIndex(i, if_not_exists=True).compile(dialect=postgresql.dialect())).strip() + ';' for i in t.indexes] + ['']) for t in ALL_TABLES]; \
	open('src/reconx/metrics/migrations/V1__initial_schema.sql','w').write('\n'.join(out))"
	@echo "Wrote src/reconx/metrics/migrations/V1__initial_schema.sql"

.PHONY: db-init
db-init: ## Create the MongoDB indexes and the metrics tables
	$(BIN)/python -m reconx.cli init-db

.PHONY: gen-key
gen-key: ## Generate a secret-encryption key
	@$(BIN)/python -m reconx.cli gen-key

## ----------------------------------------------------------------- clean
.PHONY: clean
clean: ## Remove build artefacts and caches
	rm -rf build dist *.egg-info src/*.egg-info htmlcov .coverage \
	       .pytest_cache .mypy_cache .ruff_cache spark-warehouse metastore_db derby.log
	find . -type d -name __pycache__ -prune -exec rm -rf {} + 2>/dev/null || true
