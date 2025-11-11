# 1.    Create a class called Rectangle with attributes length and width. 
# Implement a method within the class to calculate the area of the rectangle. 
# Instantiate an object of the Rectangle class with length = 5 and width = 3, and print its area.

class rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print('The area is: ', self.length * self.width)

x = rectangle(5,3)
# rectangle.area(x) 

# 2.  Create a class called Employee with attributes name and salary. 
# Implement a method within the class that increases the salary of the employee by a given percentage. 
# Instantiate an object of the Employee class with name = "John" and salary = 5000, increase the salary by 10%, and print the updated salary.

class employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def _raise(self):
         print(self.salary * 1.1)

john = employee("John", 5000)
# employee._raise(john)
