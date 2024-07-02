#!/bin/bash
echo "[*] Saving pod name..."
kubectl get pods -n ns-kcl-tnt01-audmsa-services-01 > google-cloud-sql-pods.txt
x=$(grep -w "aud-sourcefeed-scheduler-*" google-cloud-sql-pods.txt)
var="${x%% *}"
echo "[*] Connecting to PostgreSQL database..."
kubectl port-forward pod/$var 6432:5432 -n ns-kcl-tnt01-audmsa-services-01