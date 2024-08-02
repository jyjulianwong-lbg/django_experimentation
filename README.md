# The Django skeleton project
This contains experimental code that defines the structure of future AARP standardised modules. There is a main Django web app (simulating the main AARP container), connections to various Google Cloud services, and code that triggers various AARP standardised modules (e.g. Ingestion, Pre-processing etc.).

## About AARP standardised modules
AARP standardised modules are Kubernetes (K8s) Jobs that are triggered on demand by the main AARP container in a K8s cluster. A "Job" is usually a one-off task to process a piece of data / file.

There are certain files and scripts that **all** AARP standardised modules need in their code base. These can be found in the [Django skeleton repository](https://github.com/jyjulianwong-lbg/django_experimentation). These include:
```
- google-app-creds/
  # The Google Cloud credentials used when running this module locally.
- helm/charts/google_cloud_resources/
  # Various K8s ConfigMaps and Secrets that help simulate running this module in a GCP environment.
- helm/charts/module_template/
  # A template K8s YAML manifest for deploying K8s Jobs with all the Google Cloud resources connected.
- helm/Chart.yaml
- google-cloud-connect-helper.sh
  # A dependency of google-cloud-connect-helper.sh.
- google-cloud-connect.sh
  # Used for port-forwarding SQL requests from your local machine to the AARP K8s cluster where there is a centrally-hosted Cloud SQL database.
```