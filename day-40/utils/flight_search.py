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
        try:
            data = response.json()['data'][0]
        except IndexError:
            print(f'No Direct flights were found to {iata} from {self.from_airport}')
            params['max_stopovers'] = 1
            # Look up with 1 stopover
            try:
               data = response.json()['data'][0]
            except IndexError:
                print(f'No flights were found to {iata} from {self.from_airport}')
                return None 
            else:
                flight = fd(
                    destination_city=data['route'][0]['cityFrom'],
                    destination_airport=data['route'][0]['flyTo'],
                    leave_date=data['route'][0]['local_departure'].split('T')[0],
                    return_date=data["route"][1]["local_departure"].split("T")[0],
                    price=data['price'],
                    stopovers=1,
                    via_city=data['route'][0]['cityTo']
                )
                return flight
        else:
            flight = fd(
                destination_city=data['route'][0]['cityFrom'],
                destination_airport=data['route'][0]['flyTo'],
                leave_date=data['route'][0]['local_departure'].split('T')[0],
                return_date=data["route"][1]["local_departure"].split("T")[0],
                price=data['price']
            )
        return flight
