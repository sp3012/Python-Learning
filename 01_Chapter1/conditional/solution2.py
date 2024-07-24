# Movie ticket pricing

# movie tickets are priced based on age: $12 for adults(18 and above), $8 for children. Everyone gets a $2 discount on wednesday

age = int(input("Enter age: "))
day = input("Enter today's day: ")

# if age < 18 and day == "wednesday":
#     print("Price of the ticket is $6")
# elif age < 18:
#     print("Price of the ticket is $8")
    
# elif age >= 18 and day == "wednesday":
#     print("Price of the ticket is $10")

# else:
#     print("Price of the ticket is $12")

# another method

price = 12 if age >= 18 else 8

if day == "Wednesday":
    price = price - 2
    
print("Ticket price is $", price)