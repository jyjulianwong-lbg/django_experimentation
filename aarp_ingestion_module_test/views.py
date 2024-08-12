import yaml
from django.conf import settings
from django.http.response import HttpResponse
from django.urls import reverse
from django.shortcuts import HttpResponseRedirect
from kubernetes import client, config

# Create your views here.
def index(request):
    return HttpResponse(
        "Either <tt>trigger_ingestion</tt> has completed, or you haven't triggered the Ingestion container yet."
    )

def trigger_ingestion(request):
    rtl_env = settings.RTL_ENV
    if rtl_env is None:
        # Web app is most likely being run on a local machine.
        config.load_kube_config(config_file="C:\\Install\\.kube\\config")  # TODO: Update this to where your config file is.
        callback_addr = "http://host.minikube.internal:8000/aarp_ingestion_module_test/on_ingestion_completion"
    if rtl_env == "bld":
        # Web app is most likely being run within a container.
        config.load_incluster_config()
        core_v1 = client.CoreV1Api()
        service = core_v1.read_namespaced_service(name="django-experimentation-bld-service", namespace="default")  # TODO: This has been hard-coded.
        callback_addr = f"http://{service.spec.cluster_ip}:8000/aarp_ingestion_module_test/on_ingestion_completion"

    env_vars = {
        "AARP_INGESTION_CALLBACK_ADDR": callback_addr,
        "AARP_INGESTION_JOB_ID": "0000",  # TODO: This needs to be populated properly.
        "AARP_INGESTION_AUDIT_ID": "Script Development",
        "AARP_INGESTION_INPUT_PATH": "aarp/ingestion_20240730_110311_pptx-LBGTQIA.pptx",  # The Cloud storage path to the test file.
    }

    manifest_path = settings.BASE_DIR / "module_manifests" / "ingestion-bld-job.yaml"
    with open(manifest_path, "r") as file:
        job_manifest = yaml.safe_load(file)
        # TODO: Change the name of the K8s Job dynamically.
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
    if request.method == 'GET':
        return HttpResponse("You're not supposed to see this.")
    
    if request.method == 'POST':
        print("Ingestion complete! The following was returned:")
        print(request.POST)
        return HttpResponseRedirect(reverse("aarp_ingestion_module_test:index"))
