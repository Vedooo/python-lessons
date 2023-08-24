import requests as rq
from twilio.rest import Client

account_sid = 'AC9c049f525b49e831561bbd831d228fdd'
auth_token = '[AuthToken]'

URL_ENDPOINT = 'https://api.openweathermap.org/data/2.5/weather'
API_KEY= '90745f5d00287a00a0e706c6cc1326c4'
params= {
    'lat': 39.933365,
    'lon': 32.859741,
    'appid': API_KEY,
    'exclude': 'current,minutely,daily'
}

response = rq.get(URL_ENDPOINT, params=params)
response.raise_for_status()
data = response.json()
data_slice = data["hourly"][:12]

will_rain = False

for hour_data in data_slice:
    condition = hour_data["weather"][0]["id"]
    if int(condition) < 700:
        will_rain = True
    
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='+17078778461',
        body='anoncement',
        to='+905436997413'
    )
    
## https://www.pythonanywhere.com/user/vedooo/files/home/vedooo works for cloud side
## https://apilist.fun apis list