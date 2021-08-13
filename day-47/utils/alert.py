import os
import smtplib

class Notify:
    """
    Class to send some emails
    """
    def __init__(self):
        self.my_address = os.environ.get('EMAIL_ADDRESS')
        self.email_creds = os.environ.get('EMAIL_CREDS')
    

    def send_email(self, to_address, subject, msg):
        """
        Send a message from test gmail account
        """
        try:
            with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
                connection.starttls()
                connection.login(user=self.my_address, password=self.email_creds)
                connection.sendmail(from_addr=self.my_address, to_addrs=to_address, msg=f'Subject:{subject}\n\n{msg}')
        except smtplib.SMTPServerDisconnected:
            print('ERROR Unable to connect to the SMTP Server.\nEnsure your credentials are set properly')
        except smtplib.SMTPDataError:
            print(f'Email rate limit exceeded. Message to {to_address} failed.')
        else:
            print(f'Message to {to_address} sent')
