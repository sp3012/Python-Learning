# Write a Python program to print the Fibonacci sequence up to a given number using a while loop.

number = 5
fib = [0, 1]

while len(fib) < number:
    fib.append(fib[-1] + fib[-2])
    
print(fib)

# pehle 0 and 1 to fix hai fibonacci series me. isliye unko suru me le lo. then desired number tak humko feb ki list chahiye isliye hum len ka use kiya. then humne list k last k do values ko add kr dya.
