import os
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
