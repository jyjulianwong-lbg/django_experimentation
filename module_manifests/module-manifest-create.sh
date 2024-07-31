#!/bin/bash
# Fill in the following variables according to which module you would like to deploy.
RTL_ENV=bld
MODULE_NAME=ingestion
MODULE_IMAGE_REPO=tnt01-audmsa-aarp-ingestion
MODULE_SERVICE_PORT=8000
# Do not edit beyond this point unless you know what are you doing.

# Set the working directory to the Module Template Helm sub-chart.
cd ${PWD##*/}/../helm/charts/module_template

# Replace placeholder values with module-specific values as defined above.
manifest=$(helm template . --values values.yaml -s templates/job.yaml --name-template ${RTL_ENV})
manifest=${manifest//"MODULE-NAME"/$MODULE_NAME}
manifest=${manifest//"MODULE-IMAGE-REPO"/$MODULE_IMAGE_REPO}
manifest=${manifest//"MODULE-SERVICE-PORT"/$MODULE_SERVICE_PORT}

# Export the hardcoded manifest to as a new YAML file.
echo "${manifest}" > ../../../module_manifests/$MODULE_NAME-$RTL_ENV-job.yaml