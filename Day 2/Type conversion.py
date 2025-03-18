#Type conversion

num_char = len(input("What is your name? "))  #This returns an integer

print(type(num_char)) #this shows what type the above function returns (i.e int)

new_num_char = str(num_char)

print ("Your name has " + new_num_char + " characters") 


#Example 2

print(70 + float("100.5"))  #the string 100.5 converted to float