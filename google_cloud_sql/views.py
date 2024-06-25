import os

from django.db import connection
from django.http.response import HttpResponse

# Create your views here.
def index(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM pg_catalog.pg_tables;")
        data = cursor.fetchall()
    return HttpResponse(data)
