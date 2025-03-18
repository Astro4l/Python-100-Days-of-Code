#Tip Calculator

print("Welcome to the Tip Calculator")

total_bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

per_person = round(((total_bill + (total_bill * (tip_percentage / 100))) / people), 2)

# final_amount = round(per_person, 2)
final_amount = "{:.2f}".format(per_person) #This forces the result to return 2 decimal points

print(f"Each person should pay: ${final_amount}")
