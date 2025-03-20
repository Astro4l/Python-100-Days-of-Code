#Rock Paper Scissors

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
####
import random

user_choice = input("What do you choose? Type 0 for Rock, 1 for paper or 2 for Scissors.\n")
if user_choice == "0":
    print(f"You have chosen Rock\n {rock}")
elif user_choice == "1":
    print(f"You have chosen Paper\n {paper}")
elif user_choice == "2":
    print(f"You have chosen Scissors\n {scissors}")

comp_choice = random.choice([rock, paper, scissors])
print(f"The Computer chose: {comp_choice}")

if user_choice == "0" and comp_choice == scissors:
    print("You win!")
    # if comp_choice == rock:
    #     print("It's a draw!")
elif user_choice == "2" and comp_choice == paper:
    print("You win!")
    # if comp_choice == scissors:
    #     print("It's a draw!")
elif user_choice == "1" and comp_choice == rock:
    print("You win!")
    # if comp_choice == paper:
    #     print("It's a draw!")
elif user_choice == comp_choice:
    print("It's a draw!")

else:
    print("You lose!")
