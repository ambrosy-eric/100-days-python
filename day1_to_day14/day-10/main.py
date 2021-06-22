from utils.tools import operations, add_numbers, subtract_numbers, divide_numbers, multiply_numbers
from utils.art import logo

def main():
    print(logo)
    n1 = float(input('Enter a number\n'))
    for operation in operations:
        print(operation)
    more_math = True
    while more_math:
        func = input('Choose an operation\n')
        n2 = float(input('Enter a number\n'))
        try:
            result = operations[func](n1, n2)
        except Exception:
            raise(f'Invalid operation entered. {func} is not supported.')
        print(result)
        continue_calculating = input('Would you like to countinue calculating with {result}? (y/n/exit) ').lower() 
        if continue_calculating == 'y':
            n1 = result
        elif continue_calculating == 'n':
            more_math = False
            main()
        else:
            more_math = False

if __name__ == '__main__':
    main()
