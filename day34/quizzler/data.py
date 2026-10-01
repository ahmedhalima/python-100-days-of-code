import requests

parameters = {
    "amount" : 10,
    "category" : 18,
    "difficulty" : "easy",
    "type" : "boolean",
}

url = 'https://opentdb.com/api.php'
response = requests.get(url, params=parameters)
response.raise_for_status()
question_data = response.json()['results']

