# Ethan Westenskow

# Create a class called Pet with attributes name and age. 
# Implement a method within the class to calculate the age of the pet in equivalent human years. 
# Additionally, create a class variable called species to store the species of the pet. 
# Implement a method within the class that takes the species of the pet as input and returns the average lifespan for that species.

    # Instantiate three objects of the Pet class with different names, ages, and species.
    # Calculate and print the age of each pet in human years.
    # Use the average lifespan function to retrieve and print the average lifespan for each pet's species.


class Pet:
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species.lower()
    
    # https://unleashpetphotography.com/animal-age-calculator
    def human_years(self): 
        if self.species == "dog":
            return self.age * 7
        elif self.species == "goldfish":
            return self.age * 18
        elif self.species == "cat":
            return self.age * 19
        else:
            return self.age * 5

    def avg_lifespan(self):
        lifespans = { 
    "dog": 12,
    "cat": 15,
    "goldfish": 10,
        }
        if self.species.lower() in lifespans:
            return lifespans[self.species.lower()]
        else:
            return "unknown"

Winnie = Pet("Winnie", 4, "Dog")
print(f"{Winnie.name} is approximately {Winnie.human_years()} years old if in human years.")
print(f"The average lifespan for a {Winnie.species} is {Winnie.avg_lifespan()}.")

Mitch = Pet("Mitch", 7, "Dog")
print(f"{Mitch.name} is approximately {Mitch.human_years()} years old if in human years.")
print(f"The average lifespan for a {Mitch.species} is {Mitch.avg_lifespan()}.")


Spirit = Pet("Spirit", 4, "Goldfish")
print(f"{Spirit.name} is approximately {Spirit.human_years()} years old if in human years.")
print(f"The average lifespan for a {Spirit.species} is {Spirit.avg_lifespan()}.")



        