# 7. Sum of Digits: Write a Python program to calculate the sum of digits of a number using a while loop.

number = 1898734
sum = 0

for i in str(number):
    integer = int(i)
    sum += integer
    
print(sum)