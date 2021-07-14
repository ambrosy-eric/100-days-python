import os
import requests

class Nutritionix():
    """
    Class to interface with teh Nutritionix API
    """

    def __init__(self, token, gender='male', weight_kg=90.72, height_cm=188, age=30):
        self.token = token
        self.gender = gender
        self.weight_kg = weight_kg
        self.height_cm = height_cm
        self.age = age
        self.app_id = os.environ.get('NUT_ID')
        self.url = 'https://trackapi.nutritionix.com/v2'
        self.headers = {'x-app-id': self.app_id, 'x-app-key': self.token}

    def exercise_calculation(self, exercise):
        """
        Given an exercise performed
        Return json object from that exercise
        """
        url = f'{self.url}/natural/exercise'
        params = {
            'query': exercise,
            'gender': self.gender,
            'weight_kg': self.weight_kg,
            'height_cm': self.height_cm,
            'age': self.age
        }
        response = requests.post(url, headers=self.headers, json=params)
        exercise = response.json()
        data = {}
        for activity in exercise['exercises']:
            data['exercise'] = activity['name']
            data['duration'] = activity['duration_min']
            data['calories'] = activity['nf_calories']
        return data
