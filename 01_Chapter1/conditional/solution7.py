# coffee customization
# customize a coffee order: "Small", "Medium" or "Large" with an option of "Extra Shot" of espresso

size = "Medium"
extra_shot = True

if extra_shot:
    order = size + " with extra espresso shot"

else:
    order = size + "coffee"

print(order)