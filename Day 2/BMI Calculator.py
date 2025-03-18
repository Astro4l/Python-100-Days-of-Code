#BMI Calculator
#Final figure should be a whole number

height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")

bmi = int(weight) / (float(height) * float(height)) # float(height) ** 2

# print (type(bmi))
bmi_as_int = str(int(bmi))
print("Your BMI is " + bmi_as_int)