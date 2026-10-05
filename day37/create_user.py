import requests
import os
from dotenv import load_dotenv
load_dotenv()

# create a pixela user
pixela_endpoint = "https://pixe.la/v1/users"
username = os.environ.get('PIXELA_USERNAME')
token = os.environ.get('PIXELA_TOKEN')
user_params = {
    "agreeTermsOfService" : "yes",
    "notMinor":"yes",
    "username": "phpcodertop",
    "token": "V:;CWl;Ct4h("
}
user_response = requests.post(pixela_endpoint, json=user_params)
user_response.raise_for_status()
print(user_response.json())