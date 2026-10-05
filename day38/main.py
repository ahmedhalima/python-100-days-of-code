from datetime import datetime
import os

import requests
from dotenv import load_dotenv

load_dotenv()

api_id = os.environ.get('NUTRITION_API_ID')
api_key = os.environ.get('NUTRITION_API_KEY')
sheety_api_header_auth = os.environ.get('SHEETY_API_AUTH')

api_base_url = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"

auth_headers = {
    "Content-Type": "application/json",
    "x-app-id": api_id,
    "x-app-key": api_key
}
exercise_text = input("Tell me which exercises you did: ")

workout_details = {
    "query": exercise_text
}
response = requests.post(api_base_url, json=workout_details, headers=auth_headers)
response.raise_for_status()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")
for exercise in response.json()["exercises"]:
    workout_data = {
        "workout" : {
            "date" : today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration" : exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheety_api_url = "https://api.sheety.co/db401ffad73ec66a44ce8fb7126e2c86/myWorkoutsPythonCourse/workouts"
    sheety_api_headers = {
        "Authorization" : sheety_api_header_auth
    }
    sheety_response = requests.post(sheety_api_url, json=workout_data, headers=sheety_api_headers)
    sheety_response.raise_for_status()
    print(sheety_response.json())