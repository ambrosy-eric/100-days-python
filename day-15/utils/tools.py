from .data import resources, MENU

def get_resources():
    """
    Format resources
    Return formatted resources for stdout
    """
    water = resources['water']
    milk = resources['milk']
    coffee = resources['coffee']
    if 'money' not in resources.keys():
        money = 0
    else:
        money = resources['money']
    return water, milk, coffee, money

def run_report():
    """
    Given a set of resorces
    Print their current values to stout
    """
    water = resources['water']
    milk = resources['milk']
    coffee = resources['coffee']
    if 'money' not in resources.keys():
        money = 0
    else:
        money = resources['money']
    print(f'Water: {water}ml')
    print(f'Milk: {milk}ml')
    print(f'Coffee: {coffee}g')
    print(f'Money: ${money}')

def check_resources(coffee):
    """
    Given a type of coffee
    Check if the machine has enough resources to produce it
    Return True if so
    """
    required_resources = MENU[coffee]['ingredients']
    for ingredient in required_resources:
        if required_resources[ingredient] >= resources[ingredient]:
            return False
    return True

def find_igredient(coffee):
    """
    Provided a type of coffee
    Determine what resources is depleted
    Return that resource as a string
    """
    required_resources = MENU[coffee]['ingredients']
    for ingredient in required_resources:
        if required_resources[ingredient] <= resources[ingredient]:
            return ingredient

def handle_change():
    """
    Ask user for coins to insert
    Return total USD value inserted
    """
    money = 0
    print('Please insert coins.')
    money += int(input('How many quarters?: ')) * .25
    money += int(input('How many dimes?: ')) * .10
    money += int(input('How many nickels?: ')) * .05
    money += int(input('How many pennies?: ')) * .01
    return money

def verify_purchase(coffee, money):
    """
    Given a coffee type
    And amount of money
    Return True if the money > required cose
    """
    if money >= MENU[coffee]['cost']:
        return True
    else:
        return False

def make_purchase(coffee, money):
    """
    Given a type of coffee and money
    Check if the money is greater than the coffee cost
    If so, return change
    """
    if verify_purchase(coffee, money):
        change = round(money - MENU[coffee]['cost'], 2)
    else:
        change = 'refund'
    return change

def deduct_resources(coffee):
    """
    Given a coffee type fullfilled
    Deducted the required resources
    """
    new_resources = {}
    for ingredient in MENU[coffee]['ingredients']:
        new_resources[ingredient] = resources[ingredient] - MENU[coffee]['ingredients'][ingredient]
    new_resources['money'] = MENU[coffee]['cost']
    for key in new_resources:
        if key in resources:
            if key == 'money':
                resources[key] += new_resources[key]
            else:
                resources[key] -= new_resources[key]
        elif key == 'money':
            resources['money'] = new_resources[key]
