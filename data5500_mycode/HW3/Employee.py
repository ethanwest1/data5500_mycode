# Ethan Westenskow

# Create a class called Employee with attributes name and salary. 
# Implement a method within the class that increases the salary of the employee by a given percentage. 
# Instantiate an object of the Employee class with name = "John" and salary = 5000, increase the salary by 10%, and print the updated salary.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def increase_ten(self):
        self.salary = self.salary * 1.1
        return self.salary 

John = Employee("John", 5000)
print(John.increase_ten())
