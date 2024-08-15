<<<<<<< HEAD
# 3. Leap Year:
# Write a program to check if a given year is a leap year.

year = int(input("Enter the year: "))

if ( year%4 == 0 and year%100 != 0) or (year%400 == 0):
    print("Leap Year")
else:
=======
# 3. Leap Year:
# Write a program to check if a given year is a leap year.

year = int(input("Enter the year: "))

if ( year%4 == 0 and year%100 != 0) or (year%400 == 0):
    print("Leap Year")
else:
>>>>>>> 1572a0ca7fbf37fdd673ee612c85c19d878933a9
    print("NOT a leap year")