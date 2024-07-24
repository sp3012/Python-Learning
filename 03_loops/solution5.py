# Given a string. Find first non repeated character.

str = "teeteracdsacd"

for i in str:
    if str.count(i) == 1:
        print(i)
        break