import os

from django.conf import settings
from django.http.response import HttpResponse
from google.cloud import storage
from google.oauth2 import service_account
from storages.backends.gcloud import GoogleCloudStorage

# Create your views here.
def using_google_apis(request):
    if os.path.exists(settings.BASE_DIR / "service.json"):
        credentials = service_account.Credentials.from_service_account_file(settings.BASE_DIR / "service.json")
        client = storage.Client(project=settings.GS_PROJECT_ID, credentials=credentials)
    else:
        client = storage.Client(project=settings.GS_PROJECT_ID)
    
    bucket = client.get_bucket(settings.GS_BUCKET_NAME)
    path = "aarp/16b88f90-408b-4a75-8a54-0b20e42004a2"
    blob = bucket.blob(path)
    blob_content = blob.download_as_string()
    return HttpResponse(blob_content)

def using_django_storages(request):
    storage_2 = GoogleCloudStorage()
    path = "aarp/16b88f90-408b-4a75-8a54-0b20e42004a2"
    blob = storage_2.bucket.blob(path)
    blob_content = blob.download_as_string()
    return HttpResponse(blob_content)

    # blob_data = {
    #     "chunk_size": blob.chunk_size,
    #     "content_encoding": blob.content_encoding,
    #     "content_type": blob.content_type,
    #     "etag": blob.etag,
    #     "id": blob.id,
    #     "owner": blob.owner,
    #     "time_created": blob.time_created,
    # }

    # content = blob.download_as_text()
    # response = HttpResponse(content, content_type='application/octet-stream')
    # response['Content-Disposition'] = f'attachment: filename="{blob.name}"; filename*=UTF-8\'\'{blob.name}'
    # return response
    
    # with blob.open("r") as f:
    #     return HttpResponse(f.read())
    # client = storage.Client(project="tnt01-audcda-bld-01")
    # bucket_name = "tnt01-audcda-bld-01-stb-euwe2-aarp"
    # bucket = client.get_bucket(bucket_name)

    # blobs = [i for i in storage.bucket.list_blobs()]
    # return blobs
