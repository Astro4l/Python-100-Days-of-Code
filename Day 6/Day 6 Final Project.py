#Day 6 Final Project

# Reeborg's Maze

def turn_right():
    turn_left()
    turn_left()
    turn_left()


while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()

# This solves most cases but fails in some edge cases....should come back to it 
# on Day 15 to test against provided cases