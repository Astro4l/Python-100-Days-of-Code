#Paint Area Calc

import math

def paint_calc(height, width, cover):
    area = height * width
    num_of_cans = math.ceil(area / cover) #Rounding UP
    print(f"You'll need {num_of_cans} cans of paint.")


test_h = int(input("Height of the wall: "))
test_w = int(input("Width of the wall: "))
coverage = 5

paint_calc(height = test_h, width = test_w, cover = coverage)