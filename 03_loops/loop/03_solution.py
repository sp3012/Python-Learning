# 3. Write a Python program to find the sum of all even numbers in a list using a for loop.

my_list = [1, 4, 5, 3, 6, 9, 6, 8, 10, 2]
sum = 0

for i in my_list:
    if (i % 2) == 0:
        sum += i
print(sum)