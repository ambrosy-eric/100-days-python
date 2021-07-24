def add_numbers(n1, n2):
    """
    Given 2 numbers
    Return their value added together
    """
    return float(n1 + n2)

def subtract_numbers(n1, n2):
    """
    Given 2 numbers
    Return the value of the second number subracted from the first
    """
    return float(n1 - n2)

def multiply_numbers(n1, n2):
    """
    Given 2 numbers
    Return their value multiplied together
    """
    return float(n1 * n2)

def divide_numbers(n1, n2):
    """
    Given 2 numbers
    Return the value from the first number divided by the second
    """
    return n1 / n2

operations = {
    '+': add_numbers,
    '-': subtract_numbers,
    '*': multiply_numbers,
    '/': divide_numbers
}
