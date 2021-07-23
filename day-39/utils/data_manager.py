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

    def get_destination_data(self):
        """
        GET all data in the sheet and format
        """
        response = requests.get(self.url, headers=self.headers)
        data = response.json()
        self.destination_data = data['flights']
        return self.destination_data

    def update_entry(self, entry):
        """
        Takes a row number as STR and updates the corresponding row in the spreadsheet.
        """
        edit_url = f"{self.url}/{entry['id']}"
        body = {
            "flights": {
                "iataCode": entry["iataCode"]
            }
        }
        response = requests.put(url=edit_url, json=body, headers=self.headers)
