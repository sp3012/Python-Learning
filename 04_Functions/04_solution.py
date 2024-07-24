# 4. Function Returning Multiple Values
# Problem: Create a function that returns both the area and circumference of a circle given its radius.

import math

def circle (num):
    area = math.pi * (num ** 2)
    formated_area = '{:.3f}'.format(area)
    circumference = 2*math.pi*num
    formated_circumference = f"{circumference:.2f}"
    return formated_area, formated_circumference
a, c = circle(7)
print(f"Area: {a}, Circumference: {c}")

# yaha per humne format k do alag method use kiye hai. basically jaise hum string ko format krte hai same wahi wala syntax hai, bas isme hum : dete hai jo btata hai ki ab yaha se tum log kis style me tumhe format krna hai uska specification de sakte ho. then . ne bataya ki hume . se suru krna hai or . ke baad ki 2 ya 3 value tak hume chahiye.