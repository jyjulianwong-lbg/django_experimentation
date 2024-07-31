# Overview
This folder contains all the K8s specifications / manifests for the various modules in the AARP standardisation architecture, e.g. Ingestion, Pre-processing etc.

Each module would be spun up as a K8s Job on demand by the main AARP container according to the specifications of these YAML manifests.

# How to generate a new module manifest
In the case that you have developed a new standardised module for AARP, you will want to generate a K8s Job manifest for deploying it on demand.

### Pre-requisites
Run the following in a Git Bash terminal:
```
minikube start
eval $(minikube docker-env)
```

### Build the Docker image for the module
You will need to do this within the repository of your module.
```
cd /path/to/module/root/
docker build . -t <module-image-repo>:latest
```

### Generate the manifest using a Bash script
Temporarily, uncomment the entirety of `helm/charts/module_template/templates/job.yaml`.

There is a Bash script in this folder that helps to automatically generate K8s manifests for your module - `module-manifest-create.sh`.

Open this Bash script and edit the variables at the top of the script according to the details of your module.

Run the following:
```
cd /path/to/this/root/module_manifests/
sh module-manifest-create.sh
```
You should now see a new YAML file being created in the `module_manifests/` directory. Use this YAML file to spin up a new instance of your module on demand.

# File descriptions
### `ingestion-bld-job.yaml`
Refer to the [AARP Ingestion Module](https://github.com/lbg-gcp-foundation/tnt01-audmsa-aarp-ingestion).

### `preprocessing-bld-job.yaml`
This has not been implemented yet.