import re
from abc import ABC, abstractmethod

# Abstract Class
class Transport(ABC):
    @abstractmethod
    def display_info(self):
        pass

# Base Class
class Vehicle(Transport):
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.set_year(year)
    
    def set_year(self, year):
        # Regular Expression to validate that year is a four-digit number
        if not re.match(r'^\d{4}$', str(year)):
            raise ValueError("Year must be a four-digit number.")
        self.year = year
    
    def display_info(self):
        print(f"Vehicle Info: {self.year} {self.make} {self.model}")

# Derived Class
class Car(Vehicle):
    def __init__(self, make, model, year, number_of_doors):
        super().__init__(make, model, year)
        self.number_of_doors = number_of_doors

    def display_info(self):
        print(f"Car Info: {self.year} {self.make} {self.model} with {self.number_of_doors} doors")

# Exception Handling and Demonstration
try:
    # Creating instances
    vehicle = Vehicle("Toyota", "Corolla", 2020)
    car = Car("Honda", "Civic", 2018, 4)
    
    # Displaying information (Polymorphism)
    vehicle.display_info()
    car.display_info()
    
    # Testing exception handling with an invalid year
    invalid_vehicle = Vehicle("Ford", "Mustang", "20AB")
except ValueError as e:
    print(f"Error: {e}")

# Validating the correct year format with regular expressions
try:
    correct_vehicle = Vehicle("Tesla", "Model 3", 2022)
    correct_vehicle.display_info()
except ValueError as e:
    print(f"Error: {e}")
