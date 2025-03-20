#Banker Roulette

names_string = input("Please give me everybody's names, separated by a comma and a space. ")
names = names_string.split(",")
#Test
#print(names)

import random
random_name = random.choice(names)

print(f"{random_name} is going to pay for the meals today!")