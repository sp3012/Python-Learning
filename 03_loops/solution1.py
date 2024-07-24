# counting positive numbers
# Given a list of numbers count how many positive numbers.

numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
positive_number_count = 0

for num in numbers:
    if num > 0:
        positive_number_count += 1

print("The total number of positve numbers are: ", positive_number_count)