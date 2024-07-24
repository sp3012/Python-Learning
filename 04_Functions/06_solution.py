# 6. Lambda Function
# Problem: Create a lambda function to compute the cube of a number.

def cube (num):
    return num ** 3
print(cube(3))

# normally hum is tarah se function likhte hai, pr kya ho agar humara function ab ek hi baar call hona h, kuki is function ko hum baar baar call kr skte h. lekin kuki hume bs ek hi baar call krna hai to fir lambda function ka use aata h. isme hum function ko ek variable me store krte hai or wahi us function ka naam  bhi hota h.

# isme lambda likh k parameter dete hai, then seedhe : k baad apna function ka logic likho same line me.

cube = lambda num: num**3
print(cube(4))