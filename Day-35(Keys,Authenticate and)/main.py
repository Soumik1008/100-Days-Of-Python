import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = '69f04e4613056b159c2761a9d9e664d2'
account_sid = 'AC4eff551258c3f22bb4a8dd847cf3330f'
auth_token = '117c72fd44d7ce59cdb4acd8dd3160a3'

weather_params = {
    "lat":21.501360,
    "lon":86.923943,
    "appid":api_key,
    "exclude":"current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data['weather'][0]['id']
    if condition_code < 700:
        will_rain = True
        
if will_rain:
    client = Client(account_sid,auth_token)
    message = client.messages.create(
  body = 'Bring an Umbrella☂️. Its raining today Bunty',
  from_='+14178042475',
  to='+918129150342'
)
    
print(message.status)
# print(weather_data['hourly'][0]["weather"][0])