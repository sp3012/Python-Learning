# Reverse a String: Write a Python program to reverse a given string without using built-in functions like reverse() or slicing.

str = "shubham"

reversed = ""

# for char in str:
#     reversed = char + reversed 

# print(reversed)

### another method

# for char in range((len(str)) -1, -1, -1):
#     reversed = reversed + str[char]
    
# print(reversed)

for i in str[::-1]:
    reversed += i
    
print(reversed)

# agar hum range k method se krte hai to wo hume index value dega or fir hume us index ki value ko lena hoga, but agar hum slice ke method se krenge to hum ulta slicing krke direct element ki value ko le skte h.