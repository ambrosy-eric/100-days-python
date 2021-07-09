import os
import requests
from twilio.rest import Client

def get_onestop_data(location):
    """
    Given a dictionary of your longitude and latitude
    Query openweathermap's one stop api for data
    Return the dictionary from api
    """
    token = os.environ.get('TOKEN')
    url = 'http://api.openweathermap.org/data/2.5/onecall'
    params = {'lat': location['latitude'], 'lon': location['longitude'], 'appid': token}
    r = requests.get(url, params)
    if r.status_code == 200:
        return r.json()
    else:
        r.raise_for_status()

def check_hourly_rain(weather_data):
    """
    Given weather data
    Check if it is going to rain in the next 12 hours
    Return Bool
    """
    hourly_forcast = weather_data['hourly']
    for hour in hourly_forcast[:13]:
        for weather in hour['weather']:
            if weather['id'] < 600:
                return True
                
def send_sms(msg, phone_number):
    """
    Given a message and a phone number
    Send an SMS message to that phone number with your message
    """
    account_sid = os.environ.get('TWILIO_SID')
    auth_token = os.environ.get('TWILIO_TOKEN')

    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=msg,
        from_=os.environ.get('TWILIO_NUMBER'),
        to=phone_number
    )
    if message.status == 'sent':
        print('message_sent')
    elif message.status == 'queued':
        print('message queued')
