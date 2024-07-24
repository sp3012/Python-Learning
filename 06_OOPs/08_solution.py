# Class Methods

# Create a class Student with a class attribute school_name.
# Define a class method change_school_name that changes the value of school_name.
# Create an instance of Student, print the school name, use the class method to change the school name, and print the new school name.

class Student:
    school_name = "Navodaya"

    @classmethod
    def change_school_name(cls, new_name):
        cls.school_name = new_name
        
my_student = Student()

print(my_student.school_name)
Student.change_school_name("New Navodaya")

print(my_student.school_name)