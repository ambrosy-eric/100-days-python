from utils.menu import Menu, MenuItem
from utils.coffee_maker import CoffeeMaker
from utils.money_machine import MoneyMachine

def main():
    money = MoneyMachine()
    coffee_machine = CoffeeMaker()
    menu = Menu()
    is_on = True
    while is_on:
        options = menu.get_items()
        choice = input(f'What would you like? ({options}): ')
        if choice == 'off':
            is_on = False
        elif choice == 'report':
            coffee_machine.report()
            money.report()
        else:
            drink = menu.find_drink(choice)
            if coffee_machine.is_resource_sufficient(drink):
                if money.make_payment(drink.cost):
                    coffee_machine.make_coffee(drink)
            else:
                is_on = False

if __name__ == '__main__':
    main()
