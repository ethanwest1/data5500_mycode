# 3 Pillars of Object Oriented:
#     -Encapsulation: Protect your data from mis-use
#     -Inheritance: Objects can have a 'Parent-Child Relationship'
#     -Poly Morphism

# INHERITANCE:
#   -Let's us extend/ change the functionality of the parent class. 

# Inheritance Example:

class Car:
    def __init__(self, make, model, year, current_mileage, original_price): #self is the constructor
        self.make = make
        self.model = model
        self.year = year
        self.current_mileage = current_mileage
        self.original_price = original_price

    def __str__(self):
        return str(self.year) + " " + self.make + " " + self.model
    
    def calc_curr_value(self, current_year):
        age = current_year - self.year
        return  self.original_price * (.94 ** age)

andy = Car('Toyota', 'Sequoia', 2001, 310000, 40000)
print(andy)

Ethan_car = Car('Toyota', 'Tacoma', 2019, 105000, 30000)
print(Ethan_car)
print(andy.calc_curr_value(2025))
print(Ethan_car.calc_curr_value(2025))



class AntiqueCar(Car): #AntiqueCar is a child class of the class 'Car'. It inherits everything from the Car class
    def calc_curr_value(self, current_year):
        age = current_year - self.year
        return  self.original_price * (1.03 ** age)

calebs_car = AntiqueCar('Subaru', 'Forester', 2011, 106000, 25000)
print(calebs_car)
print(calebs_car.calc_curr_value(2025))


