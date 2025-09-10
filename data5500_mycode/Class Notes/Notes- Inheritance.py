# 3 Pillars of Object Oriented:
#     -Encapsulation: Protect your data from mis-use
#     -Inheritance: Objects can have a 'Parent-Child Relationship'
#     -Poly Morphism

# INHERITANCE:
#   -Let's us extend/ change the functionality of the parent class. 

# Inheritance  Class Example:

# class Car:
#     def __init__(self, make, model, year, current_mileage, original_price): #self is the constructor
#         self.make = make
#         self.model = model
#         self.year = year
#         self.current_mileage = current_mileage
#         self.original_price = original_price

#     def __str__(self):
#         return str(self.year) + " " + self.make + " " + self.model
    
#     def calc_curr_value(self, current_year):
#         age = current_year - self.year
#         return  self.original_price * (.94 ** age)

# andy = Car('Toyota', 'Sequoia', 2001, 310000, 40000)
# print(andy)

# Ethan_car = Car('Toyota', 'Tacoma', 2019, 105000, 30000)
# print(Ethan_car)
# print(andy.calc_curr_value(2025))
# print(Ethan_car.calc_curr_value(2025))



# class AntiqueCar(Car): #AntiqueCar is a child class of the class 'Car'. It inherits everything from the Car class
#     def calc_curr_value(self, current_year):
#         age = current_year - self.year
#         return  self.original_price * (1.03 ** age)

# calebs_car = AntiqueCar('Subaru', 'Forester', 2011, 106000, 25000)
# print(calebs_car)
# print(calebs_car.calc_curr_value(2025))

#My own example (taken from encapsulation notes.)
class Person:
    def __init__(self, first_name, crush):
        self.first_name = first_name
        self.__crush = crush

    #getter - Since we’ve locked the crush away, we now need a window to look at it. A getter method is that window. It lets us peek at the value safely, but still keeps control inside the class.
    def get_crush(self): 
        return self.__crush

    #setter - This is like a door to change the crush. Instead of letting people outside the class change it however they want, we give them a controlled way to do it. Later, we could even add rules — for example, reject empty names or check types.
    def set_crush(self, new_crush):
        self.__crush = new_crush

    def expose_crush(self):
        return f"{self.first_name} has a crush on {self.__crush}."


Ethan_Person = Person("Ethan", "Sarah")

class Cute_or_Not(Person):
    def out_of_league(self, rating):
        crush = self.get_crush()
        if rating > 8:
            print(f"{crush} is out of your league.")
        else: 
            print(f"Play Ball!")

Ethan_Person1 = Cute_or_Not("Ethan", "Mary")
print(Ethan_Person1.out_of_league(9))

Ethan_Person1 = Cute_or_Not("Ethan", "Lily")
print(Ethan_Person1.out_of_league(8))
