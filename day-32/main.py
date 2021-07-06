import os
import datetime as dt
import smtplib
from utils.tools import monday_quote, birthday_letter, send_email

def main():
    my_address = os.environ.get('EMAIL_ADDRESS')
    password = os.environ.get('EMAIL_CREDS')

    now = dt.datetime.now()
    current_day = now.weekday()

    connection = smtplib.SMTP('smtp.gmail.com', port=587)
    connection.starttls()
    connection.login(user=my_address, password=password)

    quote = monday_quote(current_day)
    if quote:
        send_email(connection, my_address, my_address, 'Monday Inspiration', quote)

    birthday = birthday_letter(now)
    if birthday:
        send_email(connection, my_address, birthday[0], 'Happy Birthday', birthday[1])

if __name__ == '__main__':
    main()
