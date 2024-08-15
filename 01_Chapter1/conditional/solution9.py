<<<<<<< HEAD
# Leap year checker
# Determine if a year is a leap year. (Leap years are devisible by 4, but not by hundered unless also divisible by 400)

year = int(input("Enter any year: "))

if year % 100 == 0:
    if year%400 == 0:
        print("Yes its a leap year and a century as well")
    else:
        print("Its not a leap year")
    exit()

if year % 4 == 0:
    print("Yes its a leap year")
    
else:
=======
# Leap year checker
# Determine if a year is a leap year. (Leap years are devisible by 4, but not by hundered unless also divisible by 400)

year = int(input("Enter any year: "))

if year % 100 == 0:
    if year%400 == 0:
        print("Yes its a leap year and a century as well")
    else:
        print("Its not a leap year")
    exit()

if year % 4 == 0:
    print("Yes its a leap year")
    
else:
>>>>>>> 1572a0ca7fbf37fdd673ee612c85c19d878933a9
    print("Its not a leap year")