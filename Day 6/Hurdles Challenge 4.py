# Hurdles Challenge 4

# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json

# Properly proud of this one :)

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    while  is_facing_north() == True and wall_on_right() == True:
        move()
    turn_right()
    move()
    turn_right()
    move()
    while front_is_clear() == True:
        move()
    else:
        turn_left()
   
while not at_goal():
   
    if front_is_clear() == True:
        move()
    else:
        jump()