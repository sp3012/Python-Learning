# 18. Create a function merge_dicts that merges two dictionaries into one.

def merge_dicts (dict1, dict2):
    merged_dict = dict1.copy()
    merged_dict.update(dict2)
    return  merged_dict

dict1 = {'a':1 , 'b':3}
dict2 = {'b':5 , 'c':4}

result = merge_dicts(dict1, dict2)

# print(result)

# dict1.copy() jo dict1 ki copy bana dega taki dict1 ki values affect na ho.
# fir merged wali me humne dict2 ko update kr dya, or jo key common hogi uski value dict2 wali ki value se overite kr di jaegi.

def merge_dicts (dict1, dict2):
    return {**dict1, **dict2}

dict1 = {'a':1 , 'b':3}
dict2 = {'b':5 , 'c':4}

result = merge_dicts(dict1, dict2)

# print(result)

# **dict is for unpacking a dictionary's key-value pairs into another context, such as merging dictionaries or passing as function arguments.
# **kwargs is for defining functions that can accept an arbitrary number of keyword arguments, which are collected into a dictionary within the function.


x = 99
def func ():
    x = 12
    return x
    
print(func())
print(x)