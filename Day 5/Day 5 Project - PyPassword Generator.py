#Day 5 Project - PyPassword Generator

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

letter_count = int(input("How many letters would you like in your password?\n "))
symbol_count = int(input("How many symbols would you like?\n "))
number_count = int(input("How many numbers would you like?\n "))

#Easy Level - characters come in order

password = ""
for letter in range(1, letter_count + 1):
    password += random.choice(letters)
   # print(password)
for symbol in range(1, symbol_count + 1):
    password += random.choice(symbols)
    #print(password)
for number in range (1, number_count + 1):
    password += random.choice(numbers)
print (f"Your password is: {password}")

#Hard Level - randomized order of characters

pass_chars = list(password)
random.shuffle(pass_chars)
strong_password = ''.join(pass_chars)
print(f"Your random password is: {strong_password}")