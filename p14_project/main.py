# Project 14 - Coffee Maker with OOP

# Include imports
from art import logo
from coffee_maker import CoffeeMaker
from menu import Menu, MenuItem
from money_machine import MoneyMachine

# Define Constants
menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

coffee_types = menu.get_items().split("/")

# Functions definitions
def print_list_of_coffees():
    """
    A function to print all types of supported coffees to the operator.
    :return: None
    """

    print("List of coffee types you can choose from:\n")
    print(f'\t*) Espresso. -> ${round(menu.find_drink("espresso").cost, 2)}')
    print(f'\t*) Latte. -> ${round(menu.find_drink("latte").cost, 2)}')
    print(f'\t*) Cappuccino. -> ${round(menu.find_drink("cappuccino").cost, 2)}\n')
    print('Please type the coffee of your choosing.')
    print('Please type "Off" to exit prompt and turn off the machine.')
    print('Please type "Report" to generate a report of leftover resources in the machine.')

def coffee_logic(coffee_type):
    """
    Main logic.
    :param coffee_type: type of coffee the user wants to get
    :return: True or False based on if the payment is accepted and the resources are sufficient.
    """
    if coffee_maker.is_resource_sufficient(menu.find_drink(coffee_type)):
        payment_accepted = money_machine.make_payment(menu.find_drink(coffee_type).cost)
        if payment_accepted:
            coffee_maker.make_coffee(menu.find_drink(coffee_type))
            return True
    return False

# Main Module

# Output logo
print(logo)

# Initial greeting
print("Welcome to the Coffee Machine!")
print("Machine turned on.")

# Provide the prompt in a loop to serve the next customer automatically
more_customers = True
while more_customers:
    # Prompt the user to choose an item from the list
    print("Please choose a coffee from the list below: ")
    print_list_of_coffees()
    coffee_prompt = input("What would you like to have? ").lower()

    # Validate input
    if coffee_prompt == "off":
        # If the user wants to exit, turn off the machine
        more_customers = False
        break
    elif coffee_prompt == "report":
        pass
        # If the user wants a report, generate a list of ingredients
        coffee_maker.report()
        money_machine.report()
    elif coffee_prompt not in coffee_types:
        print("Invalid input provided!")
        break
    else:
        # If the coffee chosen is within the supported ones, run the main logic
        print("Great choice!")
        coffee_logic(coffee_prompt)

# Output exit label
print("Machine turned off.")
