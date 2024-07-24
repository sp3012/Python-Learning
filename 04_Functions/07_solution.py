# 7. Function with *args
# Problem: Write a function that takes variable number of arguments and returns their sum.

# maan lo ki hume nahi pata ki hum kitne arguments dene wale hai ya fir user kitne bhi argumnets apne hisab se de skta h, to us condition me hume function ko kaise btae ki bhai tere pass kafi sare arguments aa sakte h.

# is condition me *args ka use aata h. ye * batata h function ko ki bhai muje nahi pata kitne lekin kafi arguments aa sakte hai.

def sum_all (*args):
    return sum(args) #yaha per ek inbuilt function hoata h python me sum ka wo use kiya hai.

print(sum_all(1, 2, 5, 3))
print(sum_all(1, 3))
print(sum_all(1, 4, 6, 4, 8, 6, 9, 6, 5, 3, 6))