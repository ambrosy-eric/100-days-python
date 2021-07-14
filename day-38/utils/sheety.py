import os
import datetime
import requests

class Sheety():
    """
    Class for interfacing with the sheety.co api
    """
    def __init__(self, token):
        self.token = token
        self.url = os.environ.get('SHEETY_URL')
        self.date = self.get_date()[0]
        self.time = self.get_date()[1]
        self.headers = {'Authorization': f'Bearer {token}'}

    def get_date(self):
        """
        Get the currnet date and time
        Return as Date(dd/MM/yyyy) and time (hh:mm:ss)
        """
        now = datetime.datetime.now()
        date = now.date().strftime('%d/%m/%Y')
        time = now.time().strftime('%H:%M:%S')
        return date, time

    def post_to_sheet(self, data):
        """
        Given some json data
        Post to the url
        """
        body = {
            'workout': {
                'date': self.date,
                'time': self.time,
                'exercise': data['exercise'].title(),
                'duration': data['duration'],
                'calories': data['calories']
            }
        }
        response = requests.post(self.url, headers=self.headers, json=body)
