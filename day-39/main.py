import os
from utils.data_manager import DataManager
from utils.flight_search import FlightSearch
from utils.notification_manager import NotificationManager

def main():
    data_manager = DataManager(os.environ.get('SHEETY_KEY'))
    flight_search = FlightSearch(os.environ.get('TEQUILA_TOKEN'))
    twilio = NotificationManager(os.environ.get('TWILIO_TOKEN'))

    sheet = data_manager.get_destination_data()

    for city in sheet:
        flight = flight_search.search_flights(city['iataCode'])
        if flight.price != None and flight.price <= city['lowestPrice']:
            twilio.send_sms(flight, os.environ.get('TEST_NUMBER'))

    

if __name__ == '__main__':
    main()
