# Random Module

import random

random_integer = random.randint(1, 10) #includes 1 and 10

print(random_integer)

#Random float
random_float = random.random() # between 0.0 and 1.0 but NOT including 1
print(random_float)

#If you would like to go past the 0-1 limit, you can multiply the result 
#by a certain integer. e.g To get a randomfloat btwn 0 and 5;

random_float = random.random() # between 0.0 and 1.0 but NOT including 1
random_float *= 5
print(random_float)