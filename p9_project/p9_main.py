# Project 9 - Calculator App

# Include imports
from art import logo, list_of_equations


# Function definitions - add, substract, multiply, divide and power
def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


def power(num1, num2):
    return num1 ** num2


def leftover(num1, num2):
    return num1 % num2


# Use a dictionary to store the functions by their operation sign
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "^": power,
    "%": leftover,
}


# Create a function for a new instance of a calculator
def calculator():
    # Initial greeting and logo
    print(logo)
    print("Welcome to the Calculator App!")

    # Prompt the user to input a number
    initial_num = float(input("What number would you input first? "))

    # Store the final sum and add the initial value
    final_sum = initial_num

    # While the user does calculations in the same equation, save them in the sum
    same_calculation = True
    while same_calculation:
        # Prompt for the user to choose and operator
        print("Please pick an operator from the list below:")
        print(list_of_equations)
        chosen_operator = input("Input your choice: ")

        # Validate the input
        if chosen_operator not in operations:
            print("Invalid input, exiting...")
            break

        # Prompt the operator to input another number
        next_num = float(input("What number would you input next? "))

        # Do the calculation
        final_sum = operations[chosen_operator](initial_num, next_num)

        # Output the final sum
        print(f"Equation: {initial_num} {chosen_operator} {next_num} = {final_sum}.")
        print(f"Your result is: {final_sum}")

        # Ask the operator if they would like to continue the equation
        prompt = input(f'Would you like to continue calculating with the sum of {final_sum}? Type "yes" or "no". ').lower()

        # Validate the prompt input
        if prompt == "no":
            # If a new set of numbers is requested, create a new instance
            calculator()
            # To avoid recursion, we use another return statement here
            same_calculation = False
            return
        elif not prompt == "yes":
            print("Invalid input provided, exiting...")
            return
        else:
            # If the operator wants to continue, they will use the collected sum until now
            initial_num = final_sum


# Initialize the program
calculator()



