from utils.tools import run_report, check_resources, handle_change, make_purchase, deduct_resources, find_igredient
from utils.art import coffee_emoji

def main():
    machine_on = True
    while machine_on:
        coffee = input('What would you like? (espresso/latte/cappuccino): ').lower()
        if coffee == 'report':
            run_report()
        elif coffee == 'off':
            print('Shutting down')
            machine_on = False
        else:
            if check_resources(coffee):
                money = handle_change()
                change = make_purchase(coffee, money)
                if type(change) == float:
                    print(f'Here is ${change} in change')
                    print(f'Here is your {coffee} {coffee_emoji} Enjoy!')
                    deduct_resources(coffee)
                else:
                    print('Sorry that is not enough money. Refunding your purchase')
            else:
                depleted = find_igredient(coffee)
                print(f'Sorry there is not enough {depleted}')

if __name__ == '__main__':
    main()
