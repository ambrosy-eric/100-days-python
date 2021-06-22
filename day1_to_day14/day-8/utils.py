import string

alphabet = list(string.ascii_lowercase)

def leave_in_place(character):
    """
    Given a character
    If not a ascii letter
    return True
    """
    if character not in alphabet:
        return True

def ceasar_cipher(text, cipher, direction):
    """
    Given text, an int for a cipher and direction
    Either encode or decode text
    Returning the result
    """
    ceasar_text = ''
    while cipher > len(alphabet):
        cipher -= len(alphabet)
    if direction == 'decode':
        for letter in text:
            if leave_in_place(letter):
                ceasar_text += letter
            else:
                position = alphabet.index(letter)
                shift = position - cipher
                new_letter = alphabet[shift]
                ceasar_text += new_letter
    else:
        for letter in text:
            if leave_in_place(letter):
                ceasar_text += letter
            else:
                position = alphabet.index(letter)
                shift = position + cipher
                if shift < len(alphabet):
                    new_letter = alphabet[shift]
                    ceasar_text += new_letter
                else:
                    shift -= len(alphabet)
                    new_letter = alphabet[shift]
                    ceasar_text += new_letter
    return ceasar_text
