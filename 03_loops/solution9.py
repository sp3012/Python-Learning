# List uniqueness checker
# Check if all the elements in the list are unique. If a duplicate is found, exit the loop and print the duplicate.
 
items = ["apple", "banana", "orange", "apple", "mango"]

unique_item = set()
# yaha humne set lya hai kuki set apne ander kewal unique value ko hi rakhta h.

for i in items:
    if i in unique_item:
        print(f"{i} is a duplicate item")
    
    else:
        unique_item.add(i)
print(unique_item)