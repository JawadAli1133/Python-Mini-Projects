from twilio.rest import Client

ACC_ID = 'AC56bb9e0cd96e48af5c973b115cd91324'
AUTH_TK = '5cad41ec93723829e31feebea056bd7b'


class NotificationManager:
    def __init__(self, flight):
        self.flight = flight

    def send_message(self):
        body = (f'Low price alert! Only {self.flight.price}'
                f' from {self.flight.origin_airport}'
                f' to {self.flight.destination_airport},'
                f' on {self.flight.departure_date}'
                f' until {self.flight.arrival_date}')
        client = Client(ACC_ID, AUTH_TK)
        client.messages.create(
            body=body,
            from_='+12295973444',
            to='+923260111641'
        )

