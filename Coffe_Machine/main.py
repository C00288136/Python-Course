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


def resources_sufficient(order):
    for item in order:
        if order[item] > resources[item] :
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def proccess_coins():
    print("Inset Coins")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

def transaction_successful(money_recieved, price):
    if money_recieved >= price:
        change = round(money_recieved - price, 2)
        global income 
        income += price
        return change
    
    
def make_coffee(coffee,ingredients):
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {coffee}. ENJOY")
    

machine_on = True
income = 0
while machine_on:
    user_choice = input("What drink would you like to make (espresso, latte, cappuccino) : ")
    if user_choice.lower() == 'off':
        machine_on = False
        print("Machine is turning off")
    elif user_choice.lower() == "report":
        for item in resources:
            print(f"{item} : {resources[item]}")
            
    else:
        drink = MENU[user_choice]
        if resources_sufficient(drink):
            payment = proccess_coins()
            if transaction_successful(payment,drink["cost"]):
                make_coffee(user_choice,drink["ingredients"])
                
        
            
    
    

