import os
from twilio.rest import Client

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
