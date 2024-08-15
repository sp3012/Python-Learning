<<<<<<< HEAD
# 17. Implement a function is_palindrome that checks if a given string is a palindrome.

# def is_palindrome (item):
#     reversed = item[::-1]
#     if reversed == item:
#         return ("Palindrome")
#     else:
#         return ("Not palindrome")
    
# print(is_palindrome("racecar"))


# item = "shubham"

# print(item[::-1])


def is_pallindrome (item ):
    reversed = ""
    for char in item:
        reversed = char + reversed
        
    if reversed == item:
        return "YES"

    else:
        return "NO"
    
print(is_pallindrome("racecar"))
=======
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
>>>>>>> 1572a0ca7fbf37fdd673ee612c85c19d878933a9
