#Multiple if statements in succession

# Nested if & elif statements

print ("Welcome to the Rollercoaster!")
height = int(input("What is your height in cm? "))
bill =0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print ("Child tickets are $5.")
    elif age <= 18 :
        bill = 7
        print ("Youth tickets are $7.")
    else:
        bill = 12
        print ("Adult tickets are $12.")

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3
        # if age < 12:
        #     print ("You will pay a total of $8.")
        # if age <= 18:
        #     print ("You will pay a total of $10.")
        # if age > 18:
        #     print ("You will pay a total of $15.")
    
    print(f"Your will pay a total of ${bill}")
else:
    print("Sorry, You have to grow taller before you can ride.")