#Ethan Westenskow

# 1.    Create a class called Rectangle with attributes length and width. 
# Implement a method within the class to calculate the area of the rectangle. 
# Instantiate an object of the Rectangle class with length = 5 and width = 3, and print its area.


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

test = Rectangle(3,5)
print(test.area())
