<<<<<<< HEAD
# 10. Recursive Function
# Problem: Create a recursive function to calculate the factorial of a number.

def factorial (num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)

=======
# 10. Recursive Function
# Problem: Create a recursive function to calculate the factorial of a number.

def factorial (num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)

>>>>>>> 1572a0ca7fbf37fdd673ee612c85c19d878933a9
print(factorial(5))