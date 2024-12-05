MENU = {
    "e": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "l": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "c": {
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
    'Money': 0
}


def start():
    selection = input("What would you like? (e/l/c):\n")
    if selection == 'off':
        print("System exiting.")
        exit()
    elif selection == 'report':  # TODO print ml g & $ values
        print(f"Water: {resources['water']}ml\n")
        print(f"Milk: {resources['milk']}ml\n")
        print(f"Coffee: {resources['coffee']}g\n")
        print(f"Money: ${resources['Money']}ml\n")
    else:
        is_enough = resources_check(MENU[selection])
        if is_enough == True:
            coins(selection)
        else:
            print(f"Sorry there is not enough {is_enough}.")
            start()


def resources_check(drink):
    for key in drink['ingredients']:
         if drink['ingredients'][key] > resources[key]:
             return key
    return True


def coins(drink):
    cost = MENU[drink]['cost']
    print(f"The drink you have selected costs: ${cost}")
    print("Please insert coins.\n")
    quarters = int(input('How many quarters?:\n'))
    dimes = int(input('How many dimes?:\n'))
    nickels = int(input('How many nickels?:\n'))
    pennies = int(input('How many pennies?:\n'))
    payment = 0.25 * quarters + 0.10 * dimes + 0.05 * nickels + 0.01 * pennies
    if payment < cost:
        print("Sorry that's not enough money. Money refunded.")
        start()
    elif payment > cost:
        change = round(payment - cost, 2)
        print(f"Here is ${change} in change.")
        transaction(cost, drink)
    else:
        transaction(cost, drink)


def transaction(cost, drink):
    resources['Money'] += cost
    for key in MENU[drink]['ingredients']:
        resources[key] -= MENU[drink]['ingredients'].get(key)
    print(f"Here is your {drink}. Enjoy!")
    start()


start()
