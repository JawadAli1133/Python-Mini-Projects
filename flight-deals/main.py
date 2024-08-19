from flight_search import FlightSearch
from data_manager import DataManager
import flight_data
from notification_manager import NotificationManager
import datetime as dt
from pprint import pprint

Origin_LocationCode = 'LON'

data_manager = DataManager()
sheety_data = data_manager.get_destination_data()

flight = FlightSearch()

tomorrow_date = dt.datetime.now() + dt.timedelta(days=1)
six_months_from_today = dt.datetime.now() + dt.timedelta(days=(6*30))
for city in sheety_data:
    # print(f'Checking cheapest flight for {city['city']}')
    destination_code = city['iataCode']

    flights = flight.check_flights(Origin_LocationCode,
                                   destination_code,
                                   tomorrow_date,
                                   six_months_from_today)
    cheapest_flight = flight_data.find_cheapest_flight(flights)
    print(f'The cheapest flight is from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport} in'
          f' {cheapest_flight.price} Expected Price {city['lowestPrice']}')
    if cheapest_flight.price != 'N/A' and cheapest_flight.price < float(city['lowestPrice']):
        notification_manager = NotificationManager(cheapest_flight)
        notification_manager.send_message()
        print('Message sent successfully')
    else:
        print(f'Not find any flight for {city['city']}')












