import requests
import os

class DataManager:
    """
    This class is responsible for talking to the Google Sheet.
    """
    def __init__(self, token):
        self.token = token
        self.url = os.environ.get('SHEETY_URL')
        self.headers = {'Authorization': f'Bearer {token}'}
        self.destination_data = {}

    def get_destination_data(self, worksheet):
        """
        Given a tab in the google sheet
        GET all data in the sheet and format
        """
        response = requests.get(self.url+worksheet, headers=self.headers)
        data = response.json()
        self.destination_data = data[worksheet]
        return self.destination_data

    def update_entry(self, entry):
        """
        Takes a row number as STR and updates the corresponding row in the spreadsheet.
        """
        edit_url = f"{self.url}/flights/{entry['id']}"
        body = {
            "flights": {
                "iataCode": entry["iataCode"]
            }
        }
        response = requests.put(url=edit_url, json=body, headers=self.headers)

    def add_user(self, first_name, last_name, email):
        """
        Given some user details
        Add that to the user tab in the google sheet
        """
        body = {
            'user': {
                'firstName': first_name,
                'lastName': last_name,
                'email': email
            }
        }
        response = requests.post(self.url+'users', json=body, headers=self.headers)
