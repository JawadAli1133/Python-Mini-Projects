import requests
from twilio.rest import Client


ACC_ID = 'AC56bb9e0cd96e48af5c973b115cd91324'
AUTH_TK = '5cad41ec93723829e31feebea056bd7b'

API_KEY = '8f871008f5adbed653b7cb0ee22d708d'
parameters = {
    'lat': 30.973141,
    'lon': 72.474358,
    'appid': API_KEY,
    'cnt': 4

}
response = requests.get(url='https://api.openweathermap.org/data/2.5/forecast', params=parameters)
response.raise_for_status()
data = response.json()['list']


def check_for_rain():
    for item in data:
        if item['weather'][0]['id'] < 700:
            return True
    return False


if check_for_rain():
    client = Client(ACC_ID, AUTH_TK)
    msg = client.messages.create(
        body='It is going to rain bring an ☔',
        from_='+12295973444',
        to='+923260111641')
else:
    print("There is no need to bring umbrella")
