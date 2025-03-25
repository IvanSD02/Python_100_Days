# Project 13 - Coffee Maker

# Include imports
from art import logo
from data import resources, money, MENU

# Constants definitions
coffee_types = ["espresso", "latte", "cappuccino"]


# Function definitions
def print_list_of_coffees():
    """
    A function to print all types of supported coffees to the operator.
    :return: None
    """

    print("List of coffee types you can choose from:\n")
    print(f'\t*) Espresso. -> ${MENU["espresso"]["cost"]}0')
    print(f'\t*) Latte. -> ${MENU["latte"]["cost"]}0')
    print(f'\t*) Cappuccino. -> ${MENU["cappuccino"]["cost"]}0\n')
    print('Please type the coffee of your choosing.')
    print('Please type "Off" to exit prompt and turn off the machine.')
    print('Please type "Report" to generate a report of leftover resources in the machine.')


def generate_report():
    """
    Output the list of the current resources inside the machine.
    :return: None
    """
    print("Current resources:\n")
    print(f'\tWater: {resources["water"]}')
    print(f'\tMilk: {resources["milk"]}')
    print(f'\tCoffee: {resources["coffee"]}')
    print(f'\tMoney: {money["value"]}\n')


def check_ingredient(coffee, ingredient):
    """
    Check if there are sufficient resources of this ingredient left in the machine.
    :param coffee: type of coffee the user wants to get
    :param ingredient: the given ingredient
    :return: True or False, based on if the resources are sufficient or not
    """
    return float(MENU[coffee]["ingredients"][ingredient]) <= float(resources[ingredient])

def reduce_ingredient(coffee, ingredient):
    """
    Reduce the ingredient if a coffee of a certain type is purchased.
    :param coffee: type of coffee the user wants to get
    :param ingredient: the given ingredient
    :return: None
    """
    resources[ingredient] -= MENU[coffee]["ingredients"][ingredient]


def check_resources(coffee_type):
    """
    Check if the resources in the machine are sufficient to buy the coffee.
    :param coffee: type of coffee the user wants to get
    :return: True or False, based on if the ingredients are sufficient
    """
    if coffee_type == "espresso":
        return check_ingredient(coffee_type, "water") and check_ingredient(coffee_type, "coffee")
    return check_ingredient(coffee_type, "water") and check_ingredient(coffee_type, "milk") and check_ingredient(coffee_type,"coffee")


def reduce_resources(coffee_type):
    """
    Reduce the ingredients, if a coffee of this type is made.
    :param coffee_type: type of coffee the user wants to get
    :return: None
    """
    if not coffee_type == "espresso":
        reduce_ingredient(coffee_type, "milk")
    reduce_ingredient(coffee_type, "water")
    reduce_ingredient(coffee_type, "coffee")


def process_coins():
    """
    Prompt the user to insert coins and then return the sum.
    :return: the sum of the value of all coins
    """
    # Prompt the user to insert coins
    print("Now prepare your coins and say how much you will put into the machine.\n")

    # While prompting, save the value of the money from each coin in a variable
    quarters = int(input("How many quarters do you have? ")) * 0.25
    dimes = int(input("How many dimes do you have? ")) * 0.10
    nickels = int(input("How many nickels do you have? ")) * 0.05
    pennies = int(input("How many pennies do you have? ")) * 0.01

    # Return the final sum of given money
    return quarters + dimes + nickels + pennies


def coffee_logic(coffee_type):
    """
    Main logic.
    :param coffee_type: type of coffee the user wants to get
    :return: None
    """
    if check_resources(coffee_type):
        money_given = process_coins()
        coffee_cost = MENU[coffee_type]["cost"]
        if money_given >= coffee_cost:
            print(f"Drink purchased! You have a change of ${round(money_given - coffee_cost, 2)}.\n")
            money["value"] += coffee_cost
            reduce_resources(coffee_type)
        else:
            print(f"Sorry that's not enough money(${round(money_given, 2)}). You need ${coffee_cost}. Money refunded.\n")
    else:
        print("Resources insufficient! Sorry for the inconvenience. Exiting...\n")


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
    chosen_coffee = input("What would you like to have? ").lower()

    # Validate input
    if chosen_coffee == "off":
        # If the user wants to exit, turn off the machine
        more_customers = False
        break
    elif chosen_coffee == "report":
        # If the user wants a report, generate a list of ingredients
        generate_report()
    elif chosen_coffee not in coffee_types:
        print("Invalid input provided!")
        break
    else:
        # If the coffee chosen is within the supported ones, run the main logic
        print("Great choice!")
        coffee_logic(chosen_coffee)


# Output exit label
print("Machine turned off.")

