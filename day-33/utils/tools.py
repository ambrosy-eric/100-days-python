import requests
import datetime as dt

def find_iss():
    """
    Find the latitude and longitude of the ISS
    Return a dictionary containing those
    """
    iss_location = {}

    url = 'http://api.open-notify.org/iss-now.json'
    
    r = requests.get(url=url)
    if r.status_code == 200:
        data = r.json()
        iss_location['latitude'] = float(data['iss_position']['latitude'])
        iss_location['longitude'] = float(data['iss_position']['longitude'])
    else:
        r.raise_for_status()

    return iss_location

def my_suncycle(location):
    """
    Given a location with longitude and latitude in a dictionary
    Return time of location's sunset and sunrise in UTC
    """
    lat = location['latitude']
    lng = location['longitude']
    daycycle = {}

    url = 'https://api.sunrise-sunset.org/json'
    params = {'lat': lat, 'lng':lng, 'formatted':0}

    r = requests.get(url, params=params)
    
    if r.status_code == 200:
        data = r.json()['results']
        daycycle['sunrise'] = data['sunrise']
        daycycle['sunset'] = data['sunset']
    
    return daycycle

def determine_night(daycycle):
    """
    Given a dict of sunset and sunrise times
    Determine if it is night at the current UTC time
    Return True if night
    """

    now_utc = dt.datetime.now(dt.timezone.utc)
    current_hour = now_utc.hour
    current_min = now_utc.minute

    sunrise_hour = int(daycycle['sunrise'].split('T')[1].split(':')[0])
    sunrise_min = int(daycycle['sunrise'].split('T')[1].split(':')[1])

    sunset_hour = int(daycycle['sunset'].split('T')[1].split(':')[0])
    sunset_min = int(daycycle['sunset'].split('T')[1].split(':')[1])

    if current_hour > sunset_hour:
        if current_hour < sunrise_hour:
            return True
    elif current_hour > sunset_hour:
        if current_hour == sunrise_hour and current_min < sunrise_min:
            return True
    elif current_hour == sunset_hour and current_min >= sunset_min:
        if current_hour < sunrise_hour:
            return True
    elif current_hour == sunset_hour and current_min >= sunset_min:
        if current_hour == sunrise_hour and current_min < sunrise_min:
            return True

def send_email(connection, my_address, to_address, subject, msg):
    """
    Send a message from test gmail account
    """
    if '.txt' in msg:
        with open(msg, 'r') as file:
            msg = file.read()
    connection.sendmail(from_addr=my_address, to_addrs=to_address, msg=f'Subject:{subject}\n\n{msg}')
