#Average Height Calculator

students_heights = input("Input a list of student height ").split()
for n in range(0,len(students_heights)):
    students_heights[n] = int(students_heights[n])
print(students_heights)

total_height = 0
for height in students_heights:
    total_height += height
print (f"Total height is {total_height} cm")

num_of_students = 0
for n in students_heights:
    num_of_students += 1
print(f"The total number of students is {num_of_students}")

average_height = round(total_height / num_of_students)
print(f"The average height for the students is {average_height}cm")