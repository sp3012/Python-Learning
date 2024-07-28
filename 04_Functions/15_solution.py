# 15. Define a function count_vowels that counts the number of vowels in a given string.

# def count_vowels (item):
#     count = 0
#     for i in item:
#         if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
#             count += 1
#     return count
        
# print(count_vowels("mona"))

str = "aeiou"

def vowel_count (item):
    if item in str:
        return "Vowel is present"

    else:
        return "Not present"
    
print(vowel_count("s"))