import requests
import random as rd

category = rd.randint(0,20)
parameters = {
    "amount": 10,
    "type": "boolean",
    "category": category
}

response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()
question_data = data["results"]
