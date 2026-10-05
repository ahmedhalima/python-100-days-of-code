import requests
import os
from dotenv import load_dotenv

load_dotenv()

# create a pixela graph
username = os.environ.get('PIXELA_USERNAME')
token = os.environ.get('PIXELA_TOKEN')
graph_name = "python"

pixela_graph_endpoint = f"https://pixe.la/v1/users/{username}/graphs"

graph_params = {
    "id": graph_name,
    "name": graph_name,
    "unit": "commit",
    "type": "int",
    "color": "momiji"
}
graph_headers = {
    "X-USER-TOKEN": token
}
graph_response = requests.post(url=pixela_graph_endpoint,
                               json=graph_params,
                               headers=graph_headers
                               )
graph_response.raise_for_status()
print(graph_response.json())