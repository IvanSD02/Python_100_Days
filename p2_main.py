# Project #2

# Initial greeting
print("Welcome to the tip calculator!")

# Request for the total bill, the tip percentage and the number of people
total_bill = float(input("What was the total bill? $"))
tip_percentage = int(input("How much tip would you like to give? (Recommended 10%-15%): "))
people_to_split = int(input("How many people to split the bill? "))

# Formula for generating the tip per person
total_tip = total_bill + total_bill * (tip_percentage / 100)
tip_per_person = total_tip / people_to_split
rounded_tip = round(tip_per_person, 2)  # Not necessary as the formatting will also round the number

# Output the tip
print(f"Each person should pay: ${rounded_tip:.2f}")
