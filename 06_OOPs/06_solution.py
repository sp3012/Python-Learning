# Class and Instance Attributes

# Create a class Employee with a class attribute company_name and instance attributes name and position.
# Create three instances of the Employee class.
# Print the company name and the details of each employee.

class Employee:
    company_name = "AngelOne Limited"

    def __init__(self, name, position):
        self.name = name
        self.position = position
     
    def details_of_employee(self):
        return(f"The {self.name} works on the position {self.position} in {Employee.company_name}")

employee_one = Employee("Shubham", "DAE")

print(employee_one.details_of_employee())