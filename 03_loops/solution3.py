<<<<<<< HEAD
# multiplication table printer 
# Print the multiplication table for a given number upto 10, but skip the 5th iteration

number = 2

for i in range(1, 11):
    if i == 5:
        continue
    else:
        table = 2*i
=======
# multiplication table printer 
# Print the multiplication table for a given number upto 10, but skip the 5th iteration

number = 2

for i in range(1, 11):
    if i == 5:
        continue
    else:
        table = 2*i
>>>>>>> 1572a0ca7fbf37fdd673ee612c85c19d878933a9
        print(f"{number} * {i} = {table}")