from random import choice

from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine=MoneyMachine()
is_order=True

coffee_maker=CoffeeMaker()

menu=Menu()

while is_order:
    options=menu.get_items()
    choice=input(f"What would you like?{options}")
    if choice=="off":
        is_order=False
    elif choice=="report":
        money_machine.report()
        coffee_maker.report()
    else:
        drink=menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            print("ok it is sufficient")
            money_machine.make_payment(drink.cost)
            coffee_maker.make_coffee(drink)

        else:
            print("no resources are sufficient")
