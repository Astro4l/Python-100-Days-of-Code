#Banker Roulette - Angela Yu

import random
names_string = input("Please give me everybody's names, separated by a comma and a space. ")
names = names_string.split(",")#split string method

items = len(names) #counts number of items in list
random_name = random.randint(0, items - 1)  # -1 because python counts from 0

victim = names[random_name]
print(f"{victim} will pay the bill!")