# Project #3

# Print the chosen ASCII Art

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')

# Initial greeting
print("Welcome to treasure island!")
print("Your sole mission is to find the treasure.")

# Input first prompt - crossroad
print("You\'re at a crossroad. Where would you like to go?")
direction = input('\t Type "left" or "right"\n').lower()  # Enable using capital letters in input as well

# Store the status of the player
alive = True

# Make a decision to continue the story based on the crossroad
if direction == "left":
    print("Wise choice. You continue down the road safely.")
elif direction == "right":
    print("You fell into a hole.")
    print("You lost. Game over!")
    alive = False
else:
    print("Invalid input provided.")
    alive = False

# If the player survived the crossroad, the next prompt is output - swim in the lake
if alive:
    print("You have come across a lake. There is an island in the middle of the lake. Will you swim to it?")
    swim_or_not = input('\t Type "swim" or "wait"\n').lower()  # Enable using capital letters in input as well

    # If the player survived the crossroad, you have to make a decision to swim to the island or not,
    # based on which the story will progress
    if swim_or_not == "wait":
        print("You dodged a bullet. You saw a small shiny platform in the distance. It looks more promising.")
    elif swim_or_not == "swim":
        print("You were attacked by trout while swimming. You suffered severe injuries.")
        print("You lost. Game over!")
        alive = False
    else:
        print("Invalid input provided.")
        alive = False

# If the player survived the lake, the next prompt is output - choosing a door
if alive:
    print("On the platform you see three doors. One is blue, one is red, the last one is yellow.\n"
          "Which one will you enter? Or will you run away?")
    door = input('\t Type "red", "blue" or "yellow". Type "none" to get away.\n').lower()  # Enable using capital letters in input as well

    # If the player survived the crossroad, you have to make a decision which door the player will enter
    if door == "red":
        print("Fire erupted spontaneously and you were burned to ashes!")
        print("You lost. Game over!")
        alive = False
    elif door == "yellow":
        print("The treasure is right in front of you! All the gold you can get!")
        print("You won! Hooray!")
    elif door == "blue":
        print("A beast appeared from behind and you were cut to pieces by its claws!")
        print("You lost. Game over!")
        alive = False
    elif door == "none":
        print("A hand appeared from below the platform, grabbed your body and dragged it to the debts of the Earth.")
        print("You lost. Game over!")
        alive = False
