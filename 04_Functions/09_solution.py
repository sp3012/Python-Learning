# 9. Generator Function with yield
# Problem: Write a generator function that yields even numbers up to a specified limit.

# def even_generator (limit):
#     for i in range(2, limit+2, 2):
#         print(i)               
# even_generator(10)

 # ab ese to kaam sahi kr raha h per hume ese print ni karana hota h actual project me. return krke function kko kahi or pr use krna hota h.


def even_generator (limit):
    for i in range(2, limit+2, 2):
        return i

# print(even_generator(10))

# for num in even_generator(10):
#     print(num)

# ab agar hum bahar laker function ko call krke print krwana chah re h to function call k baad for loop me jata h, 2 se suru krta h and then wahi 2 fir return ho jata h. or function ki property hai, ki jaise hi usko return mila to function stop ho jata h. ab print function firse even_generator ko call krta h or is baar firse function me for loop 2 se suru hoke 2 ko ki return kr deta h.

# to ab hume esa koi method chahiye jo hmare pichle wale call ko yaad rakkhe, uski memory me kya h or uski location ko yaad rakkhe. isliye yield function use hota h.


def even_generator (limit):
    for i in range(2, limit+2, 2):
        yield i

for num in even_generator(10):
    print(num)