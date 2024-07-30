import yaml
from django.conf import settings
from django.http.response import HttpResponse
from django.shortcuts import render
from kubernetes import client, config

# Create your views here.
def index(request):
    return HttpResponse(
        "Either <tt>trigger_ingestion</tt> has completed, or you haven't triggered the Ingestion container yet."
    )

def trigger_ingestion(request):
    config.load_kube_config(config_file="C:\\Install\\.kube\\config")  # TODO: Update this to where your config file is.

    manifest_path = settings.BASE_DIR / "module_manifests" / "ingestion-bld-minikube.yaml"

    env_vars = {
        "AARP_HOST_ADDR": "127.0.0.1",  # TODO: This is wrong.
        "AARP_INGESTION_JOB_ID": "0000",  # TODO: This needs to be populated properly.
        "AARP_INGESTION_AUDIT_ID": "Script Development",
        "AARP_INGESTION_INPUT_PATH": "aarp/ingestion_20240730_110311_pptx-LBGTQIA.pptx",  # The Cloud storage path to the test file.
    }

    with open(manifest_path, "r") as file:
        job_manifest = yaml.safe_load(file)
        for key, value in env_vars.items():
            job_manifest["spec"]["template"]["spec"]["containers"][0]["env"].append(
                {
                    "name": key,
                    "value": value,
                }
            )

    batch_v1 = client.BatchV1Api()

    namespace = "default"
    batch_v1.create_namespaced_job(body=job_manifest, namespace=namespace)
    
    return HttpResponse(
        "Ingestion container has been triggered. Waiting on completion..."
    )

def on_ingestion_completion(request):
    # TODO: Implement.
    pass
