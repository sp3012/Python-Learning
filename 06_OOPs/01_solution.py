# 1. Basic Class and Object Creation

# Define a class Book with attributes title, author, and year_published.
# Create three instances of the Book class with different values.
# Print out the attributes of each instance.

class Book:
    def __init__(self, title, author, year):
        self.title  = title
        self.author = author
        self.year = year
        
        
book = Book("Panchtantra", "Shubham", 2000)
new_book = Book("Comic", "Mohan", 1997)
another_new_book = Book("Yugg", "Rampal", 1888)

print(book.year)
print(new_book.title)
print(another_new_book.author)