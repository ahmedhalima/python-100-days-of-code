import random

import requests
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

# create a new pixel
username = os.environ.get('PIXELA_USERNAME')
token = os.environ.get('PIXELA_TOKEN')
graph_name = "python"

pixela_graph_endpoint = f"https://pixe.la/v1/users/{username}/graphs/{graph_name}"
graph_headers = {
    "X-USER-TOKEN": token
}
today = datetime.now()
formatted_date = today.strftime("%Y%m%d")
random_value = random.randint(5,20)
graph_data = {
    "date": formatted_date,
    "quantity":"5"
}
pixel_response = requests.post(url=pixela_graph_endpoint, json=graph_data, headers=graph_headers)
pixel_response.raise_for_status()
print(pixel_response.json())