#!/bin/bash
# Get Google Cloud credentials and set the correct K8s context.
gcloud auth login
gcloud container clusters get-credentials tnt01-audmsa-bld-01-kcl-01-euwe2 --region=europe-west2 --project=tnt01-audmsa-bld-01-fdc2
gcloud config set project tnt01-audmsa-bld-01-fdc2

echo "[*] kubectl has been changed to run in the following context:"
kubectl config get-contexts

# Automatically re-run Cloud SQL connection script when connection is broken.
until bash google-cloud-sql-connect-once.sh; do
	echo "[!] google-cloud-sql-connect-once.sh crashed with exit code $?. Respawning..." >&2
	sleep 1
done