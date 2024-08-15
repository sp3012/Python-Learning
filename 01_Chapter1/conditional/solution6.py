<<<<<<< HEAD
# transport of mode based on distance (E.g. <3km-walk, 3-15km:Bike, >15km:car

distance = int(input("Enter distance from 0 onwards: "))
mode = ""

if distance < 0:
    print("Please enter a valid distance")
    exit()

if distance < 3:
    mode = "Walk"
elif distance < 16:
    mode = "Bike"
else:
    mode = "Car"
    
=======
# transport of mode based on distance (E.g. <3km-walk, 3-15km:Bike, >15km:car

distance = int(input("Enter distance from 0 onwards: "))
mode = ""

if distance < 0:
    print("Please enter a valid distance")
    exit()

if distance < 3:
    mode = "Walk"
elif distance < 16:
    mode = "Bike"
else:
    mode = "Car"
    
>>>>>>> 1572a0ca7fbf37fdd673ee612c85c19d878933a9
print("Kindly take a", mode)