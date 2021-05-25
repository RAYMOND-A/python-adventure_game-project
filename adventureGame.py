# conditional if/else statement

# water_level = 50
# if water_level > 80:
#     print("Drain water")
# else:
#     print("continue")

# = implies we are assigning a value to a variable
# == implies we are checking to see if the value on the left equals the value on the right
# >= greater than or equal to
# <= lesser than or equal to
# != not equal to
# % modulo operator gives the remainder, e.g 7%2 is 1 


# coding exercise checking if number inputed is either an even or an odd number

print("Coding Exercise, checking if number inputed is either an even or an odd number")

number = int(input("Which number do you want to check? "))

if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")


# # Logical operators, and, or, not
# for the 'add' operator all conditions must be true, for it to output true
# for the 'or' operator atleast one of the conditions should be true, for it to output true
# the 'not' operators reverses a condition, if a condition is true it reverses it to false and vice versa


# final project
# Treasure Island
# choose your own adventure game

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

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

direction = input("You're at a cross road. Where do you want to go? Type \"left\" or \"right\"! ")

if direction.lower() == "right":
    print("Game Over, you fell into a hole")
elif direction.lower() == "left":
    continue_journey = input("You're infront of the Ocean. Do you want to swim or wait? Type \"swim\" or \"wait\"! ")
    if continue_journey.lower() == "swim":
        print("Game Over, you can't possible swim across the ocean. It is too deep and large")
    elif continue_journey.lower() == "wait":
        select_door = input("Wow great choice, now choose which of the three doors to enter. Type \"Red\" or \"Blue\" or \"Yellow\"! ")
        if select_door.lower() == "red":
            print("Game Over, you choose the wrong door, try again next time")
        if select_door.lower() == "blue":
            print("Game Over, you choose the wrong door, try again next time")
        if select_door.lower() == "Yellow":
            print("Congratulations you win")