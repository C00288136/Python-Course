import requests
import os
from twilio.rest import Client



api_key = os.environ.get("OWM_API_KEY")
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
params = {
    "lat" : 53.029160,
    "lon" :-7.320510,
    "appid" : api_key,
    "cnt": 4,
}

response = requests.get(OWM_Endpoint, params=params)


data = response.json()
will_rain = False
raindata = []

# need to first select each item in the json lib list
# 0:3 checks the 3 different libraries 
# the rest of the statment is appended to get the required data
for item in data["list"][0:3]:
    raindata.append(item["weather"][0]["id"])


print(raindata)

for item in raindata:
    if item < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
                .create(
                     body="Its going to rain today, Bring a umbrella ☔",
                     from_='+15014394409',
                     to='+353874442242'
                 )

    print(message.status)
