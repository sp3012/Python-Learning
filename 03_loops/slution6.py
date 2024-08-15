# Compute the factorial of a number using while loop

# number = 5
# factorial = 1

# i = 1

# while i <= number:
#     factorial = factorial * i
#     i += 1
    
# print(f"Factorial value of {number} is {factorial}")

# number = 5
# factorial = 1

# while number > 0:
#     factorial *= number
#     number -= 1
    
# print(f"Factorial value of is {factorial}")  

# With the for loop

number = 5 
factorial = 1

for i in range(1, number+1):
    factorial *= i
    
print(f"Factorial value of {number} is {factorial}")