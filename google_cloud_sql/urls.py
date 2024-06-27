from django.urls import path

from . import views

app_name = "google_cloud_sql"
urlpatterns = [
    path("", views.index, name="index"),
    path("django_migrations/", views.django_migrations, name="django-migrations"),
]
