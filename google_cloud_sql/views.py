import os

from django.db import connection
from django.conf import settings
from django.http.response import HttpResponse

# Create your views here.
def index(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM pg_catalog.pg_tables;")
        data = cursor.fetchall()
    return HttpResponse(f"Connected to PostgreSQL via: {settings.DB_HOST}<hr/><b>All tables in the application-db database</b>:<br/>{data}")

def django_migrations(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM django_migrations;")
        data = cursor.fetchall()
    return HttpResponse(f"Connected to PostgreSQL via: {settings.DB_HOST}<hr/><b>All rows in the django_migrations table</b>:<br/>{data}")
