from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.ai.agents.models import ListSortOrder
import os
from dotenv import load_dotenv
from azure.identity import ClientSecretCredential
from azure.core.credentials import AzureKeyCredential

load_dotenv()
endpoint = os.getenv("AZURE_EXISTING_AIPROJECT_ENDPOINT")

def login_with_environment():
    """
    Loads Azure credentials from environment variables and returns a ClientSecretCredential.
    """
    tenant_id = os.getenv("AZURE_TENANT_ID")
    client_id = os.getenv("AZURE_CLIENT_ID")
    client_secret = os.getenv("AZURE_CLIENT_SECRET")
    if not all([tenant_id, client_id, client_secret]):
        raise ValueError("Missing one or more Azure credential environment variables: AZURE_TENANT_ID, AZURE_CLIENT_ID, AZURE_CLIENT_SECRET")
    return ClientSecretCredential(tenant_id, client_id, client_secret)

def get_key_credential():
    """
    Loads API key from environment variables and returns an AzureKeyCredential.
    """
    api_key = os.getenv("AZURE_API_KEY")
    if not api_key:
        raise ValueError("Missing AZURE_API_KEY environment variable.")
    return AzureKeyCredential(api_key)

try:
    # Get project client
    project_endpoint = os.getenv("AZURE_EXISTING_AIPROJECT_ENDPOINT")
    project_client = AIProjectClient(
        credential=DefaultAzureCredential(),
        endpoint=project_endpoint,
    )

    # List all connections in the project
    connections = project_client.connections
    print("List all connections:")
    for connection in connections.list():
        print(f"{connection.name} ({connection.type})")

except Exception as ex:
    print(ex)