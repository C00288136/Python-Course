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
# make a function if the resources are sufficient 
def sufficient_resources(drink):
    for item in drink:
        if drink[item] >= resources[item]:
            print(f"Insufficient {item} for this drink")
            return False
    return True
        
# process coins function
def process_coins():
    print("Inset Coins")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

# transaction successful function

def transaction_success(total_inserted, price_drink):
    if total_inserted >= price_drink:
        change = total_inserted - price_drink
        print(f"Here is your change : ${change} ")
        global income
        income += price_drink
        return True
    else:
        print("Not enough was inserted for the drink")
        return False
# make coffee
def make_coffee(drink, ingredients):
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {drink}☕️. ENJOY")





# Prompt user by asking “What would you like? (espresso/latte/cappuccino)
income = 0
machine_on = True
while machine_on:
    user_choice = input("What would you like ? (espresso/latter/cappuccino)")   
    # turn off machine when entering 'off'
    if user_choice.lower() == "off":
        machine_on = False
    elif user_choice.lower() == "report":
        print(f"Water : {resources['water']}ml")
        print(f"Milk : {resources['milk']}ml")
        print(f"Coffee : {resources['coffee']}ml")
        print(f"Money : ${income}")
        
    else:
        drink = MENU[user_choice]
        if sufficient_resources(drink["ingredients"]):
            payment = process_coins()
            if transaction_success(payment, drink["cost"]):
                make_coffee(user_choice,drink["ingredients"])
                
            
    

# print report

