import requests
from .flight_data import FlightData as fd


class FlightSearch:
    """
    This class is responsible for talking to the Flight Search API.
    """
    def __init__(self, token):
        self.token = token
        self.url = 'https://tequila-api.kiwi.com/v2'
        self.from_airport = 'ORD'
        self.early_dept_date = '02/04/2022'
        self.max_dept_date = '22/04/2022'
        self.nights = '13'
        self.headers = {'apikey': self.token}

    def search_flights(self, iata):
        """
        Given an IATA code
        Search for flight data for trips to that airport
        """
        params = {
            'fly_from': self.from_airport,
            'fly_to': iata,
            'dateFrom': self.early_dept_date,
            'dateTo': self.max_dept_date,
            'nights_in_dst_from': self.nights,
            'nights_in_dst_to': self.nights,
            'flight_type': 'round',
            'max_stopovers': 0,
        }

        response = requests.get(self.url+'/search', headers=self.headers, params=params)
        print(iata)
        if response.json()['data'] != []:
            data = response.json()['data'][0]
            flight = fd(
                destination_city=data['route'][0]['cityFrom'],
                destination_airport=data['route'][0]['flyTo'],
                leave_date=data['route'][0]['local_departure'].split('T')[0],
                return_date=data["route"][1]["local_departure"].split("T")[0],
                price=data['price']
            )
        else:
            print(f'No direct flights found to {iata}')
            flight = fd(
                destination_city=iata,
                destination_airport=iata,
                leave_date=None,
                return_date=None,
                price=None
            )
        return flight
