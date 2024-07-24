# 6. Prime Numbers: Write a Python program to check if a given number is prime or not using a for loop.

number = 50
is_prime = True

for i in range(2, 5):
    if (number % i) == 0:
        is_prime = False
        break
print(is_prime)
