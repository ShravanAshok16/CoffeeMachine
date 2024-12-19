MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 180,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 200,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 220,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}



def resources_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}, Money Refunded")
            return False
    return True

def process_coins():
    print("Please insert coins.\n")
    total = int(input("How many 10s notes?: ")) * 10
    total += int(input("How many 20s notes?: ")) * 20
    total += int(input("How many 100s notes?: ")) * 100

    return total

def transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is INR {change}/- in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    if transaction_successful(process_coins(), MENU[choice]["cost"]):
        for item in order_ingredients:
            resources[item] -= order_ingredients[item]
        print(f"Here is your {drink_name} ☕️. Enjoy!")
    else:
        print("Transaction failed. Please try again.")

def turn_on_off():
    global should_continue
    machine_status= input("Turn on the machine? Type 'yes' or 'no':\n").lower()
    if machine_status == "yes":
        should_continue = True
    elif machine_status == "no":
        should_continue = False
    return should_continue

def generate_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: INR {profit}/-")

def refill_resources():
    resources["water"] = 300
    resources["milk"] = 200
    resources["coffee"] = 100

profit = 1000

should_continue = turn_on_off()

while should_continue:
    choice =input("What would you like? (espresso/latte/cappuccino):\n")
    if resources_sufficient(MENU[choice]["ingredients"]):
        make_coffee(choice, MENU[choice]["ingredients"])
    else:
        refill = input("Do you want to refill resources:\n").lower()
        if refill == "yes":
            refill_resources()
        elif refill == "no":
            should_continue = False

generate_report()
print("Goodbye!")
