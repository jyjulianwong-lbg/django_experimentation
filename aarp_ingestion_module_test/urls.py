from django.urls import path

from . import views

app_name = "aarp_ingestion_module_test"
urlpatterns = [
    path("", views.index, name="index"),
    path("trigger_ingestion", views.trigger_ingestion, name="trigger_ingestion"),
    path("on_ingestion_completion", views.on_ingestion_completion, name="on_ingestion_completion"),
]
