#Python Lists

fruits = ["Orange", "Apple", "Banana", "Grapes", "Pear", "Watermelon", "Kiwi"]

#Getting anitemfromthe list
print(fruits[0])
print(fruits[-1]) #starts fromthe end

#Changing an item in the list
fruits[2]= "Banananas"
print(fruits)

#Adding to the list
fruits.append("Pineapple")
print(fruits)

#Adding a list to the list
fruits.extend(["Mango", "Lemon", "Pixies"])
print(fruits)