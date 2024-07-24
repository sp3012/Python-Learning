# 11. Create a function is_prime that checks if a number is prime.

def is_prime(num):
    if num <= 1:
        return ("Not a Prime")
    for i in range(2, int(num ** 0.5)+1):
        if num % i == 0:
            return ("Not a prime")   
    return ("Prime")

print(is_prime(20))

# ab yaha per humne number of iteration km kr diye. kuki koi bhi composite number product hota h kisi do number ka. or dono number me se ek number hmesa <= hota h square root of composite number k. or baad k number firse unhi chote walo se pair bnate hai. isliye hum upto square root of n hi check krte h. 