# coffee machine

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

coins = {
    'quarters' : 0.25,
    'dimes': 0.10,
    'nickels': 0.05,
    'pennies': 0.01
}
money = 0

def get_report():

    print("Resources:")
    print(f"water : {resources['water']}ml")
    print(f"milk: {resources['milk']}ml")
    print(f"coffee: {resources['coffee']}g")
    print(f"\nCash available £{money:.2f}")

def sufficient_resources(drink):
    
    resources_okay = True
    for ingredient in MENU[drink]['ingredients']:
        if resources[ingredient] < MENU[drink]['ingredients'][ingredient]:
            print(f"There is not enough {ingredient} to make a {drink}")
            resources_okay = False
    return resources_okay

def process_coins(drink):
    global money

    cost = MENU[drink]['cost']
    total_entered = 0
    for coin in coins:
        quantity = int(input(f"Enter number of {coin} "))
        total_entered += coins[coin] * quantity
    if total_entered > cost:
        print(f"Thank you. Here is your change £{total_entered-cost:.2f}")
        money += cost
        return True
    elif total_entered == cost:
        print("Thank you. Exact amount entered.")
        money += cost
        return True
    else:
        print("Returning your money - insufficient funds.")
        return False

def make_coffee(drink):

    for resource in resources:
        resources[resource] -= MENU[drink]['ingredients'][resource]
    print(f"Enjoy your cup of {drink}")

power_on = True
while power_on:
    drink = input("\nWhat would you like? (espresso/latte/cappuccino): ")
    if drink == 'report':
        get_report()
    elif drink == 'quit':
        power_on = False
    else:
        if sufficient_resources(drink):
            if process_coins(drink):
                make_coffee(drink)
            
        
            
