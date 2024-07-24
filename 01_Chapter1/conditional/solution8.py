# Password strength checker
# Check is password is "weak", "medium" or "strong". criteria <6 char("weak"), 6-10 char ("medium"), >10 Char("strong")

password = input("Enter your password: ")

if len(password) < 6:
    strength = "Weak"
elif len(password) < 10:
    strength = "Medium"
else:
    strength = "Strong"
    
print("The strength of the password is", strength)