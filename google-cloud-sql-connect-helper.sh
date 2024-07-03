#!/bin/bash
echo "[*] Saving pod name..."
kubectl get pods -n ns-kcl-tnt01-audmsa-services-01 > google-cloud-sql-pods.txt --context gke_tnt01-audmsa-bld-01-fdc2_europe-west2_tnt01-audmsa-bld-01-kcl-01-euwe2
x=$(grep -w "aud-sourcefeed-scheduler-*" google-cloud-sql-pods.txt)
var="${x%% *}"
echo "[*] Connecting to PostgreSQL database..."
kubectl port-forward pod/$var 6432:5432 -n ns-kcl-tnt01-audmsa-services-01 --context gke_tnt01-audmsa-bld-01-fdc2_europe-west2_tnt01-audmsa-bld-01-kcl-01-euwe2