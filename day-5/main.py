## This is not a real password generator
## Printing password to terminal, not great
## Not using secrets.systemrandom, not great
## Storing symbols, letters, and numbers in list in memory is also bad
## Just the exercise which reqs allowing choosing letters, numbers, and symbols

import random
import secrets
import string

alphabet = string.ascii_letters
allowed_symbols = string.punctuation

def generate_password(letters, numbers, symbols):
    """
    Given a int for number of letters, numbers and symbols
    Generate a string with those requirements
    Return the string
    """
    if length_check(letters, numbers, symbols):
        characters = []
        for number in range(numbers):
            characters.append(str(secrets.randbelow(10)))
        for symbol in range(symbols):
            characters.append(secrets.choice(allowed_symbols))
        for letter in range(letters):
            characters.append(secrets.choice(alphabet))
        random.shuffle(characters)
        password = ''.join(characters)
        return password
    else:
        raise Exception('Please provide atleast 12 total characters for your password')

def length_check(*args):
    """
    Check the length of a potential password
    If 12 or more
    return True
    """
    result = 0
    for n in args:
        result += n
    if result >= 12:
        return True

def main():
    print("Welcome to the PyPassword Generator!")
    letters = int(input("How many letters would you like in your password?\n")) 
    symbols = int(input(f"How many symbols would you like?\n"))
    numbers = int(input(f"How many numbers would you like?\n"))
    password = generate_password(letters, symbols, numbers)
    print(password)

if __name__ == "__main__":
    main()