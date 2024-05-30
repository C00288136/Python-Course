from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine_on = True
drinks_on_menu = Menu()
coffee_maker = CoffeeMaker()
money = MoneyMachine()
while machine_on:
    user_choice = input(f"What drink would you like : {drinks_on_menu.get_items()} : ")
    if user_choice.lower() == "off":
        machine_on = False
    elif user_choice.lower() == "report":
        coffee_maker.report()
        money.report()
    else:
        drink = drinks_on_menu.find_drink(user_choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)

