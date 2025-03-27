#Sum of even numbers 1-100

total = 0
for number in range(2, 101, 2 ):
    total += number
print(total)

#Alternative way

total2 = 0
for num in range(1, 101):
    if num % 2 == 0:
        total2 += num
print (total2)
