from django.urls import path

from . import views

app_name = "google_cloud_storage"
urlpatterns = [
    path("using_google_apis/", views.using_google_apis, name="using-google-apis"),
    path("using_django_storages/", views.using_django_storages, name="using-django-storages"),
]
