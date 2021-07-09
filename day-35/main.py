import os
from utils.tools import get_onestop_data, check_hourly_rain, send_sms

def main():
    chicago = {
        'latitude': 41.878113,
        'longitude': -87.629799
    }
    if check_hourly_rain(get_onestop_data(chicago)):
        send_sms('Rain is in the forcast for today. Better bring a raincoat or umbrella!', os.environ.get('TEST_NUMBER'))

if __name__ == '__main__':
    main()
