# multiplication table printer 
# Print the multiplication table for a given number upto 10, but skip the 5th iteration

number = 2

for i in range(1, 11):
    if i == 5:
        continue
    else:
        table = 2*i
        print(f"{number} * {i} = {table}")