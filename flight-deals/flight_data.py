class FlightData:
    def __init__(self, price, origin_airport, destination_airport, departure_date, arrival_date):
        self.price = price
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.departure_date = departure_date
        self.arrival_date = arrival_date

def find_cheapest_flight(flights):

    if flights is None or not flights['data']:
        return FlightData("N/A", "N/A", "N/A", "N/A", "N/A")

    first_flight = flights['data'][0]
    lowest_price = float(first_flight['price']['grandTotal'])
    price = lowest_price
    origin_airport = first_flight['itineraries'][0]['segments'][0]['departure']['iataCode']
    destination_airport = first_flight['itineraries'][0]['segments'][0]['arrival']['iataCode']
    departure_date = first_flight['itineraries'][0]['segments'][0]['departure']['at'].split('T')[0]
    arrival_date = first_flight['itineraries'][0]['segments'][0]['arrival']['at'].split('T')[0]

    cheapest_flight = FlightData(price, origin_airport, destination_airport, departure_date, arrival_date)

    for flight in flights['data'][1:]:
        price = float(flight['price']['grandTotal'])
        if price < lowest_price:
            lowest_price = price
            origin_airport = flight['itineraries'][0]['segments'][0]['departure']['iataCode']
            destination_airport = flight['itineraries'][0]['segments'][0]['arrival']['iataCode']
            departure_date = flight['itineraries'][0]['segments'][0]['departure']['at'].split('T')[0]
            arrival_date = flight['itineraries'][0]['segments'][0]['arrival']['at'].split('T')[0]
            cheapest_flight = FlightData(price, origin_airport, destination_airport, departure_date, arrival_date)

    return cheapest_flight























