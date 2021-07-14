import os
from utils.nutritionix import Nutritionix
from utils.sheety import Sheety

def main():
    nutritionix = Nutritionix(os.environ.get('NUT_TOKEN'))
    sheety = Sheety(os.environ.get('SHEETY_KEY'))

    ## Get user input
    exercise = nutritionix.exercise_calculation(input('What exercise did you perform: '))
    sheety.post_to_sheet(exercise)

if __name__ == '__main__':
    main()
