#Love Calculator

print("Welcome to the Love Calculator!")
name_1 = input("What is your name? \n")
name_2 = input("What is their name? \n")


t_total = (name_2.lower().count("t")) + (name_1.lower().count("t"))
r_total = (name_2.lower().count("r")) + (name_1.lower().count("r"))
u_total = (name_2.lower().count("u")) + (name_1.lower().count("u"))
e_total = (name_2.lower().count("e")) + (name_1.lower().count("e"))

true_total = str(t_total + r_total + u_total + e_total)


l_total = (name_2.lower().count("l")) + (name_1.lower().count("l"))
o_total = (name_2.lower().count("o")) + (name_1.lower().count("o"))
v_total = (name_2.lower().count("v")) + (name_1.lower().count("v"))
e2_total = (name_2.lower().count("e")) + (name_1.lower().count("e"))

love_total = str(l_total + o_total + v_total + e2_total)

true_love = int(true_total + love_total)

if true_love < 10 or true_love > 90:
    print(f"Your score is {true_love}, you go together like coke and mentos!")
elif true_love >= 40 and true_love <= 50:
    print(f"Your score is {true_love}, you are alright together!")
else:
    print(f"Your score is {true_love}")


# Alternatively, combine both names into a single string to check the characters in one go 