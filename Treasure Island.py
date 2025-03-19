#Treasure Island

print("Welcome to Treasure Island \n Your mission is to find the treasure")
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
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

direction = input("You are at a crossroad, choose the left or right path: ")
if direction.lower() == "left":
    wait_or_swim = input(" You have chosen the correct path. \n You've come to a river. On the other end you can see three doors. What do you do? Swim or wait? ")
    if wait_or_swim.lower() == "wait":
        which_door = input("A boat came and you have crossed the river safely. The three doors are colored red, blue and yellow. Pick the door to enter. ")
        if which_door.lower() == "yellow":
            print("Horray! You win, you have found the treasure!")
        elif which_door.lower() == "red":
            print("Game over! You have fallen into a fire pit!")
        elif which_door.lower() == "blue":
            print ("Game over! You have been eaten by a grizzly bear!")
        else:
            print("Game over! Invalid choice.")
    elif wait_or_swim.lower() == "swim":
        print("Game over! You have been eaten by pirannas!")
    else:
        print("Game over! Invalid choice.")
elif direction.lower() == "right":
    print("Game over! You have fallen into a hole")
else:
    print("Game over! Invalid choice.")