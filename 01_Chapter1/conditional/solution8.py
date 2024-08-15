<<<<<<< HEAD
# Password strength checker
# Check is password is "weak", "medium" or "strong". criteria <6 char("weak"), 6-10 char ("medium"), >10 Char("strong")

password = input("Enter your password: ")

if len(password) < 6:
    strength = "Weak"
elif len(password) < 10:
    strength = "Medium"
else:
    strength = "Strong"
    
=======
# Password strength checker
# Check is password is "weak", "medium" or "strong". criteria <6 char("weak"), 6-10 char ("medium"), >10 Char("strong")

password = input("Enter your password: ")

if len(password) < 6:
    strength = "Weak"
elif len(password) < 10:
    strength = "Medium"
else:
    strength = "Strong"
    
>>>>>>> 1572a0ca7fbf37fdd673ee612c85c19d878933a9
print("The strength of the password is", strength)