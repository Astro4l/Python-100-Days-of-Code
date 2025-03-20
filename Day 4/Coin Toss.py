#Coin Toss

import random

face = random.choice(['head', 'tail'])

print(face)

#Angela Yu Alternative
random_side = random.randint(0, 1)
if random_side == 1:
    print("Heads")
else:
    print("Tails")