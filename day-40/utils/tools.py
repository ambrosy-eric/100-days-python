def get_user_information():
    """
    Add a user to the spreadsheet
    """
    print('Welcome to the Flight Club.\nWe find the best flight deals and email you')
    first_name = input('What is your first name? ').title()
    last_name = input('What is your last name? ').title()
    while True:
        email = input('What is your email address? ').lower()
        if '@' not in email or '.' not in email:
            print('Please enter a valid email address')
            email = input('What is your email address? ').lower()
        email_verify = input('Please confirm your email address. ').lower()
        if email == email_verify:
            print(f'Your address {email} has been set.')
            break
    
    return first_name, last_name, email