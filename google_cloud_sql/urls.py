from django.urls import path

from . import views

app_name = "google_cloud_sql"
urlpatterns = [
    path("", views.index, name="index"),
]
