# 2. Grade Calculator:
# Write a program that takes a student's score as input and prints the corresponding grade based on the following scale:
# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: Below 60

marks = int(input("Enter your marks: "))


if (marks < 0) or (marks > 100):
    print("Kindly enter valid marks")
elif marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
elif marks >= 60:
    print("Grade D")
else:
    print("Grade F")