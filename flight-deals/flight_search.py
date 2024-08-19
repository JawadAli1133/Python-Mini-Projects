import requests
from _datetime import datetime

FLIGHT_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"


class FlightSearch:
    def __init__(self):
        self.api_key = 'muy8px6nHLr1fAlGNoBKaFGZTv1ultFo'
        self.api_secret = 'PexLHuPwqBYMJqgt'
        self.bearer_token = self.get_token()

    def get_token(self):
        token_url = "https://test.api.amadeus.com/v1/security/oauth2/token"
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        data = {
            "grant_type": "client_credentials",
            "client_id": self.api_key,
            "client_secret": self.api_secret
        }
        response = requests.post(url=token_url, headers=headers, data=data)
        return response.json()['access_token']

    def get_iata_code(self, city_name):
        city_url = 'https://test.api.amadeus.com/v1/reference-data/locations/cities'
        params = {
            'keyword': city_name,
            "max": "2",
            "include": "AIRPORTS"
        }
        headers = {
            "Authorization": f"Bearer {self.bearer_token}"
        }
        response = requests.get(url=city_url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()
        return data['data'][0]['iataCode']

    def check_flights(self, origin_code, destination_code, departure_date, return_date):
        headers = {
            "Authorization": f"Bearer {self.bearer_token}"
        }
        params = {
            'originLocationCode': origin_code,
            'destinationLocationCode': destination_code,
            'departureDate': departure_date.strftime('%Y-%m-%d'),
            'returnDate': return_date.strftime('%Y-%m-%d'),
            "nonStop": "true",
            'adults': 1,
            'currencyCode': 'GBP',
            "max": "10"
        }
        response = requests.get(url=FLIGHT_ENDPOINT, params=params, headers=headers)
        response.raise_for_status()
        return response.json()



