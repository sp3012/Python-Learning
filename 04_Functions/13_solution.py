# 13. Write a function max_of_three that returns the maximum of three numbers.

def max_number(a, b, c):
    if a > b and a > c:
        return (f"{a} is greater")
    elif b > c and b > a:
        return (f"{b} is greater")
    else:
        return (f"{c} is greater")
print(max_number(3, 7, 2))