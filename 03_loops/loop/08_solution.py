# Palindrome Check: Write a Python program to check if a given string is a palindrome or not using a for loop.

str = "racecar"
compare_one = ""
compare_two = ""

# for word in range((len(str) - 1), -1, -1):
#     compare_two += str[word]

if str == compare_two:
    print("Yes")
else:
    print("NO")
    
# Another method of reversing the string:

reversed = ""
for char in str[::-1]:
    reversed += char
print(reversed)