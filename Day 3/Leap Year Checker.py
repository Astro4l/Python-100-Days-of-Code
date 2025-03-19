# Leap Year Checker

year = int(input("Please enter the year you would like to check: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print (f"The year {year} is a leap year")
        else:
            print (f"The year {year} is not a leap year")
    else:
        print (f"The year {year} is a leap year")
else:
    print (f"The year {year} is not a leap year")