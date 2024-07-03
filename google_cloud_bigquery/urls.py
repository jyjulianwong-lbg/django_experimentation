from django.urls import path

from . import views

app_name = "google_cloud_bigquery"
urlpatterns = [
    path("", views.index, name="index"),
]
