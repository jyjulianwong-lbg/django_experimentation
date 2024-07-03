from django.conf import settings
from django.http.response import HttpResponse
from google.cloud import bigquery

# Create your views here.
def index(request):
    # Override GCP project ID from the default one used in this project.
    project_id = "tnt01-audcda-bld-01-1a3a"

    # Copied over from https://codelabs.developers.google.com/codelabs/cloud-bigquery-python#6
    client = bigquery.Client(project=project_id, credentials=settings.GS_CREDENTIALS)

    query = """
        SELECT user, timestamp, run_name
        FROM `tnt01-audcda-bld-01-1a3a.tnt01_audcda_bqd_euwe2_analytics.ada_runs`
        ORDER BY timestamp DESC
        LIMIT 10
        ;
    """

    results = client.query(query=query, project=project_id)

    data = ""
    for row in results:
        user = row["user"]
        timestamp = row["timestamp"]
        run_name = row["run_name"]
        data += f"{user:<20} | {str(timestamp):<20} | {run_name:<20}<br/>"
    
    return HttpResponse(f"<b>Query</b>:<br/>{query}<hr/><b>Results</b>:<br/>{data}")
