import os
import smtplib
from utils.tools import find_iss, my_suncycle, determine_night, send_email

def main():
    my_address = os.environ.get('EMAIL_ADDRESS')
    password = os.environ.get('EMAIL_CREDS')
    
    chicago = {
        'latitude': 41.878113,
        'longitude': -87.629799
    }

    iss_location = find_iss()
    chicago_daycycle = my_suncycle(chicago)
    while determine_night(chicago_daycycle):
        if chicago['latitude'] - 5 <= iss_location['latitude'] <= chicago['latitude'] + 5 and chicago['longitude'] - 5 <= iss_location['logitude'] <= chicago['longitude'] + 5:
            connection = smtplib.SMTP('smtp.gmail.com', port=587)
            connection.starttls()
            connection.login(user=my_address, password=password)
            send_email(connection, my_address, my_address, 'ISS Present', 'Look outside to see the ISS overhead')
            connection.close() 

if __name__ == '__main__':
    main()
