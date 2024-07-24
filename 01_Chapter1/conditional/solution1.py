# Age group categorization
# Clasify a person's age group: child(<13), Teenager(13-19), Adult(20-59), Senior(60+)

entered_age = int(input("Enter your age: "))

if entered_age < 13:
    print("Child")
elif entered_age < 20:
    print("Teenager")
elif entered_age < 60:
    print("Adult")
else:
    print("senior")