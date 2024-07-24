# 16. Write a function sum_of_squares that returns the sum of the squares of a list of numbers.

def sum_of_squares (item):
    square = 0
    sum = 0
    for i in item:
        square = i ** 2
        sum += square
    return sum
    
print(sum_of_squares([3, 5, 7, 4, 1, 9, 10]))