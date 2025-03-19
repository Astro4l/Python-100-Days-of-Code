#Logical Operators

# AND
# OR 
# NOT

#Multiple if statements in succession

# Nested if & elif statements

print ("Welcome to the Rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age >= 45 and age <= 50:                             #logical operator AND
        print("You're experiencing a midlife crisis, you ride for free!")
    if age < 12:
        bill = 5
        print ("Child tickets are $5.")
    elif age <= 18 :
        bill = 7
        print ("Youth tickets are $7.")
    elif age < 45 or age > 50:                              #logical operator OR
        bill = 12
        print ("Adult tickets are $12.")

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3
    
    print(f"Your will pay a total of ${bill}")
else:
    print("Sorry, You have to grow taller before you can ride.")