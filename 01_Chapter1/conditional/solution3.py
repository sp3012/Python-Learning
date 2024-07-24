# Grade calculator
# Assign a letter grade based on a student score: A(90-100), B(80-89), C(70-79), D(60-69), F(below 60)

score = 79

grade = ""
if score >= 90 and score <= 100:
    grade = "A"
elif score >= 80 and score < 90:
    grade = "B"
elif score >= 70 and score < 80:
    grade = "C"
elif score >= 60 and score < 70:
    grade = "D"
else:
    grade = "F"
    
print("Your grade is:", grade)

# To exit any python program exit() is used. Isse hume agar kisi condition, loop ya function k baad exit hona h to hum ho sakte hai.