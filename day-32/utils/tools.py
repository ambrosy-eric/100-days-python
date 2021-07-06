import random
import pandas as pd

def monday_quote(day):
    """
    If the day is monday
    Return a random Quote
    """
    with open('./data/quotes.txt', 'r') as file:
        quotes = [line.strip('\n') for line in file]

    if day == 0:
        quote = random.choice(quotes)
        return quote

def birthday_letter(daytime):
    """
    Given a day
    Determine if any birthdays match in data/birthdays.csv
    Return a new letter
    """
    today_tuple = (daytime.month, daytime.day)
    bday_data = pd.read_csv('data/birthdays.csv')
    bday_dict = {(row.month, row.day): row for (index, row) in bday_data.iterrows()}  

    if today_tuple in bday_dict:
        name = bday_dict[today_tuple]['name']
        email = bday_dict[today_tuple].email
        letter = _write_birthday_letter(name)
        return email, letter


def _write_birthday_letter(name):
    """
    Given a name of someone celebrating a birthday
    Write a new letter celebrating their birthday
    """
    rand_letter = random.randint(1,3)
    starting_letter = open(f'./data/letter_templates/letter_{rand_letter}.txt', 'r')
    finished_letter = open(f'./outputs/{name}_birthday.txt', 'w')
    for line in starting_letter:
        finished_letter.write(line.replace('[NAME]', name))

    starting_letter.close()
    finished_letter.close()
    return f'./outputs/{name}_birthday.txt'

def send_email(connection, my_address, to_address, subject, msg):
    """
    Send a message from test gmail account
    """
    if '.txt' in msg:
        with open(msg, 'r') as file:
            msg = file.read()
    connection.sendmail(from_addr=my_address, to_addrs=to_address, msg=f'Subject:{subject}\n\n{msg}')
