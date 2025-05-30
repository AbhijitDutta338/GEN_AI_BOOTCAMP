import functions_framework
import vertexai
from vertexai.generative_models import GenerativeModel
from google.cloud import aiplatform

@functions_framework.http
def hello_http(request):
   
    request_json = request.get_json(silent=True)
    logs = request_json.get("logs", "No logs provided")

    # Initialize Vertex AI
    vertexai.init(project=os.environ.get("GCP_PROJECT"), location="us-central1")

    # Prepare the prompt
    prompt = f"""
    You are an SRE. Based on the logs below, summarize the incident and recommend a probable fix.
    Logs:
    {logs}
    """

    # Call Vertex AI
    model = GenerativeModel("gemini-2.0-flash-001")
    response = model.generate_content(prompt)

    return {"summary": response.text}
