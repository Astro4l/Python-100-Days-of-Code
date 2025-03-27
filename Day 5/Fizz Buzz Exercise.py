#Fizz Buzz Exercise

# Program should print 1-100
# For every number divisible by 3, print Fizz
# For every number divisible by 3, print Buzz
# For numbers didvisibleby bot, print FizzBuzz

for number in range (1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print ("FizzBuzz")
    elif number % 3 == 0:
        print ("Fizz")
    elif number % 5 == 0:
        print ("Buzz")
    else:
        print (number)