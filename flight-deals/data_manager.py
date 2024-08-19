import requests
from flight_search import FlightSearch

url = 'https://api.sheety.co/216142fc92e7c71f884385b09745bf16/flightDeals/prices'

class DataManager:
    def __init__(self):
        self.data = []

    def get_destination_data(self):
        get_response = requests.get(url)
        self.data = get_response.json()['prices']
        return self.data

    def update_data(self, row_id, body):
        put_url = f'{url}/{row_id}'
        put_response = requests.put(url=put_url, json=body)

    def update_iataCode(self):
        flight = FlightSearch()
        for city in self.data:
            code = flight.get_iata_code(city['city'])
            row_id = city['id']
            new_data = {
                'price': {
                    'iataCode': code
                }
            }
            self.update_data(row_id=row_id, body=new_data)



