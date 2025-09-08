# Data 5500 Notes

# 3 Pillars of Object Oriented:
#     -Encapsulation
#     -Inheritance
#     -Poly Morphism

    # Encapsulation:
    #     -The ability to protect/encapsulate data. You control how and when the data is updated. 
    #     -"__"before a variable will make it hidden. You can only update hidden data in a function that you create. 

    # Practice: (Define class + make a variable hidden)
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

    #Example of getter function - 'looking' through the window to the room with the hidden variable. 
    print(Ethan_Person.get_crush()) 

    print(Ethan_Person.expose_crush())

    #Setting a new crush
    Ethan_Person.set_crush("Emily")
    print(Ethan_Person.expose_crush())



