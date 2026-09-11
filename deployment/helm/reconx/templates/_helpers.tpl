{{/* Expand the name of the chart. */}}
{{- define "reconx.name" -}}
{{- default .Chart.Name .Values.nameOverride | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{/* Fully qualified app name. */}}
{{- define "reconx.fullname" -}}
{{- if .Values.fullnameOverride -}}
{{- .Values.fullnameOverride | trunc 63 | trimSuffix "-" -}}
{{- else -}}
{{- $name := default .Chart.Name .Values.nameOverride -}}
{{- if contains $name .Release.Name -}}
{{- .Release.Name | trunc 63 | trimSuffix "-" -}}
{{- else -}}
{{- printf "%s-%s" .Release.Name $name | trunc 63 | trimSuffix "-" -}}
{{- end -}}
{{- end -}}
{{- end -}}

{{- define "reconx.chart" -}}
{{- printf "%s-%s" .Chart.Name .Chart.Version | replace "+" "_" | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{- define "reconx.labels" -}}
helm.sh/chart: {{ include "reconx.chart" . }}
{{ include "reconx.selectorLabels" . }}
app.kubernetes.io/version: {{ .Chart.AppVersion | quote }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
app.kubernetes.io/part-of: reconx
{{- end -}}

{{- define "reconx.selectorLabels" -}}
app.kubernetes.io/name: {{ include "reconx.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end -}}

{{- define "reconx.serviceAccountName" -}}
{{- if .Values.serviceAccount.create -}}
{{- default (include "reconx.fullname" .) .Values.serviceAccount.name -}}
{{- else -}}
{{- default "default" .Values.serviceAccount.name -}}
{{- end -}}
{{- end -}}

{{- define "reconx.secretName" -}}
{{- if .Values.security.existingSecret -}}
{{- .Values.security.existingSecret -}}
{{- else -}}
{{- printf "%s-secrets" (include "reconx.fullname" .) -}}
{{- end -}}
{{- end -}}

{{/* Image reference for a component: registry + repository + tag. */}}
{{- define "reconx.image" -}}
{{- $root := index . 0 -}}
{{- $component := index . 1 -}}
{{- $image := index $root.Values.image $component -}}
{{- $tag := default $root.Chart.AppVersion $image.tag -}}
{{- printf "%s%s:%s" $root.Values.image.registry $image.repository $tag -}}
{{- end -}}

{{/* Shared env from the ConfigMap and the platform Secret. */}}
{{- define "reconx.envFrom" -}}
- configMapRef:
    name: {{ include "reconx.fullname" . }}-config
- secretRef:
    name: {{ include "reconx.secretName" . }}
{{- end -}}

{{- define "reconx.stagingClaimName" -}}
{{- if .Values.storage.staging.existingClaim -}}
{{- .Values.storage.staging.existingClaim -}}
{{- else -}}
{{- printf "%s-staging" (include "reconx.fullname" .) -}}
{{- end -}}
{{- end -}}
