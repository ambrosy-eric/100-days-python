import os
from utils.tools import get_user_information
from utils.data_manager import DataManager
from utils.flight_search import FlightSearch
from utils.notification_manager import NotificationManager

def main():
    data_manager = DataManager(os.environ.get('SHEETY_KEY'))
    flight_search = FlightSearch(os.environ.get('TEQUILA_TOKEN'))
    notify = NotificationManager(os.environ.get('TWILIO_TOKEN'))

    flights_sheet = data_manager.get_destination_data('flights')
    user_sheet = data_manager.get_destination_data('users')

    new_user = input('Are you a new user? (y/n) ').lower()
    if new_user == 'y':
        new_user_data = get_user_information()
        data_manager.add_user(first_name=new_user_data[0], last_name=new_user_data[1], email=new_user_data[2])


    for city in flights_sheet:
        flight = flight_search.search_flights(city['iataCode'])
        if flight is not None and flight.price <= city['lowestPrice']:
            notify.send_sms(flight, os.environ.get('TEST_NUMBER'))
            notify.notify_users(flight, user_sheet)

if __name__ == '__main__':
    main()
