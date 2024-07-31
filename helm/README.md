# Overview
This directory contains all the Helm charts used to deploy this project, including project-specific and AARP-common charts.

# Chart descriptions
### `google_cloud_resources`
This is an AARP-common chart used to provide Google Cloud resources (e.g. Cloud Storage, Cloud SQL etc.) to Minikube deployments (e.g. this Django project). This is considered "AARP-common" because modules deployed as K8s Jobs (e.g. Ingestion, Pre-processing etc.) will also depend on this chart in their K8s manifests. This chart contains various ConfigMaps and Secrets to connect to Google Cloud services.

### `module_template`
This is a template chart not used for deployment, but instead used to generate K8s manifests for modules (e.g. Ingestion, Pre-processing). It is dependent on `google_cloud_resources`. This chart contains a single manifest - `templates/job.yaml`. All K8s Job manifests will follow this template. See the `module_manifests/` folder for instructions on how to generate a module manifest.

### `django_experimentation`
This is the project-specific chart used to deploy this current Django project as a web app. It is dependent on `google_cloud_resources`.