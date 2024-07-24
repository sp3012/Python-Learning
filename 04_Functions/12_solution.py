# 12. Implement a function fibonacci that returns the first n numbers in the Fibonacci sequence.

list = [0, 1]

def febonacci (num):
    for i in range(num+1):
        final = list.append(list[-1] + list[-2])
    return list
print(febonacci(10))