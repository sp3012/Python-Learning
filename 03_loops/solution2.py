# Calculate sum of even numbers upto a given number n.

number = 10
sum = 0

for i in range(1, number+1):
    if i%2 == 0:
        sum += i
        
print(sum)