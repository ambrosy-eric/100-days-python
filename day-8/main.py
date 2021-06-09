import string


from utils import ceasar_cipher
from art import logo

def main():
    run_again = 'yes'
    while run_again == 'yes':
        print(logo)
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        if direction == 'encode':
            print(f'Encoded value: {ceasar_cipher(text, shift, direction)}')
        elif direction == 'decode':
            print(f'Decoded value: {ceasar_cipher(text, shift, direction)}')
        else:
            raise Exception('Invalid option provided.\nPlease select either "encode" or "decode"')
        run_again = input('Type yes if you want to go again. Otherwise type no\n')

if __name__ == '__main__':
    main()
