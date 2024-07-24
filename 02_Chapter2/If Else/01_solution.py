# 1. Odd or Even:
# Write a program to check if a given number is odd or even.

number = int(input("Enter any number: "))

if number % 2 == 0:
    print("Number", number, "is an EVEN number")
else:
    print("Number", number, "is an ODD number")