import requests as rq
from datetime import datetime

# response = requests.get('http://api.open-notify.org/iss-now.json')
# data = response.json()["iss_position"]

# longitude = data["longitude"]
# latitude = data["latitude"]

# iss_position = (latitude, longitude)

# print(iss_position)

MY_LAT = 38.963745
MY_LNG = 35.243320

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,
}

response = rq.get('https://api.sunrise-sunset.org/json', params=parameters)
data = response.json()["results"]
sunrise = float(data["sunrise"].split("T")[1].split(":")[0])
sunset = float(data["sunset"].split("T")[1].split(":")[0])

print(sunrise, sunset)

