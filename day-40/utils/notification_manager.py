import os
import smtplib
from twilio.rest import Client

class NotificationManager:
    """
    This class is responsible for sending notifications with the deal flight details.
    """
    def __init__(self, token):
        self.token = token
        self.from_number = os.environ.get('TWILIO_NUMBER')
        self.account_sid = os.environ.get('TWILIO_SID')
        self.auth_token = os.environ.get('TWILIO_TOKEN')
        self.client = Client(self.account_sid, self.auth_token)
        self.my_address = os.environ.get('EMAIL_ADDRESS')
        self.email_creds = os.environ.get('EMAIL_CREDS')

    def send_sms(self, msg, phone_number):
        """
        Given a message and a phone number
        Send an SMS message to that phone number with your message
        """
        text = f'Low Price alert! ${msg.price} to fly to {msg.destination_city}-{msg.destination_airport} \nDates: {msg.leave_date} to {msg.return_date}'
        message = self.client.messages.create(
            body=text,
            from_=self.from_number,
            to=phone_number
        )
        if message.status == 'sent':
            print('message_sent')
        elif message.status == 'queued':
            print('message queued')

    def notify_users(self, flight, users):
        """
        Notify Users of a flight deal
        """
        for user in users:
            recipient = f"{user['email']}"
            subject = f'Low Price Alert!'
            message = f'Low Price to {flight.destination_city}. Price is {flight.price}\nDates: {flight.leave_date}-{flight.return_date}'
            self._send_email(self.my_address, recipient, subject, message)

    def _send_email(self, my_address, to_address, subject, msg):
        """
        Send a message from test gmail account
        """
        try:
            with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
                connection.starttls()
                connection.login(user=self.my_address, password=self.email_creds)
                connection.sendmail(from_addr=my_address, to_addrs=to_address, msg=f'Subject:{subject}\n\n{msg}')
        except smtplib.SMTPServerDisconnected:
            print('ERROR Unable to connect to the SMTP Server.\nEnsure your credentials are set properly')
        except smtplib.SMTPDataError:
            print(f'Email rate limit exceeded. Message to {to_address} failed.')
        else:
            print(f'Message to {to_address} sent')