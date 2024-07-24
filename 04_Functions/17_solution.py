# 17. Implement a function is_palindrome that checks if a given string is a palindrome.

def is_palindrome (item):
    reversed = item[::-1]
    if reversed == item:
        return ("Palindrome")
    else:
        return ("Not palindrome")
    
print(is_palindrome("racecar"))


# item = "shubham"

# print(item[::-1])