# Overview
This folder contains all the YAML K8s specifications / manifests for the various modules in the AARP standardisation architecture, e.g. ingestion, pre-processing etc.

Each module would be spun up as a K8s Job on demand by the main AARP container according to the specifications of these manifests.

# File descriptions
### `ingestion-bld-minikube.yaml`
Refer to the [AARP Ingestion Module](https://github.com/lbg-gcp-foundation/tnt01-audmsa-aarp-ingestion). This YAML file can be generated manually by running `helm install ... --dry-run` (TODO: This does not work if the Helm charts in these 2 repositories are not synced up properly. Fix this.).