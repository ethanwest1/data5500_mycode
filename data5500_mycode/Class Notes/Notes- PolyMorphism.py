# Data 5500 Notes

# 3 Pillars of Object Oriented:
#     -Encapsulation: Protect your data from mis-use
#     -Inheritance: Objects can have a 'Parent-Child Relationship'
#     -Poly Morphism: A child can dynamically change behavior at runtime

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

# andys_car = Car('Toyota', 'Sequoia', 2001, 310000, 40000)
# print(andys_car)

# Ethan_car = Car('Toyota', 'Tacoma', 2019, 105000, 30000)
# print(Ethan_car)
# print(andys_car.calc_curr_value(2025))
# print(Ethan_car.calc_curr_value(2025))



# class AntiqueCar(Car): #AntiqueCar is a child class of the class 'Car'. It inherits everything from the Car class
#     def calc_curr_value(self, current_year):
#         age = current_year - self.year
#         return  self.original_price * (1.03 ** age)

# calebs_car = AntiqueCar('Subaru', 'Forester', 2011, 106000, 25000)
# print(calebs_car)
# print(calebs_car.calc_curr_value(2025))

# gregs_car = AntiqueCar("Cadillac", "Coupe DeVille", 1978, 150000, 15000)
# print(gregs_car)
# print(gregs_car.calc_curr_value(2025))

# #########################
# #PolyMorphism example
# #Let's say we want to calculate the value of the entire car lot. 
# zachs_car = Car("Toyota", "Camry", 2002,200000, 20000)
# alexs_car = Car("Honda", "CRV", 2013, 131000, 22000)

# car_lot = [andys_car, calebs_car, Ethan_car, gregs_car, zachs_car, alexs_car] #Car objects

# for car in car_lot: #The object decides which function runs at runtmie (Car vs AntiqueCar) (The list is full of different objects)
#     print(car.calc_curr_value(2025))


##########################
#My own example
class Skater: #parent class
    def __init__(self, name, trick, raw_score):
        self.name = name
        self.trick = trick
        self.raw_score = raw_score

    def score_calculator(self):
        score = 100 * self.raw_score
        return score

class Scooter(Skater): #Child class
    def score_calculator(self):
        score = -10 * self.raw_score
        return score

ethan = Skater('Ethan', 'Kickflip', 8)
print(ethan.score_calculator()) #Skater score_calculator works

wesly = Scooter("Wesly", "Tailwhip", 5)
print(wesly.score_calculator()) #Scooter score_calculator works

#items
leo = Skater('Leo', 'Blunt', 9)
jacob = Scooter('Jacob', 'Backflip', 10)

#PolyMorphism
skatepark = [ethan, wesly, leo, jacob] #consists of objects that call different functions.

for person in skatepark: #when ran, it runs the function that belong to the specific object.
    print(person.score_calculator())


