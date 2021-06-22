#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python

def main():
    print('Welcome to the tip calculator')
    bill = float(input('How much was the total bill in dollars?\n'))
    split = int(input('How many people are spliting the bill?\n'))
    tip = float(int(input('What % would you like to tip\n')) / 100)

    payment = (bill + (bill * tip)) / split
    amount = '{:.2f}'.format(payment)
    print(f'Each person should pay: ${amount}')

if __name__ == "__main__":
    main()
    