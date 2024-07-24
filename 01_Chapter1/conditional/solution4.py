# Determine if a fruit is ripe, overipe or unripe based on its color. (Eg. Banana: Green-Unripe, Yellow-Ripe, Brown-Overipe)

fruit_condition = ""
color = "Green"

if color == "Green":
    fruit_condition = "Unripe"
elif color == "Yellow":
    fruit_condition = "Ripe"
elif color =="Brown":
    fruit_condition = "Overipe"
    
print("The condition of the fruit is:", fruit_condition)