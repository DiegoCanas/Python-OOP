# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 08:44:59 2023

@author: dicacam
"""

#OOP Exercise 1: Create a Class with instance attributes 



class Vehicle:     
    def __init__(self, max_speed, mileage):
        self.max_speed=max_speed
        self.mileage=mileage
                
#OOP Exercise 2: Create a Vehicle class without any variables and methods

obj = Vehicle
    
class Vehicle:
    pass

#OOP Exercise 3: Create a child class Bus that will inherit all of the variables and methods of the Vehicle class

obj = Vehicle

class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        
class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo", 180, 12)
print("Vehicle Name: ", School_bus.name, "Speed:", School_bus.max_speed, "Mileage:", School_bus.mileage)

#OOP Exercise 4: Class Inheritance

class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

class Bus(Vehicle):
    def seating_capacity(self, capacity = 50):
        return super().seating_capacity(capacity)
    
School_bus = Bus("School Volvo", 180, 12)
print(School_bus.seating_capacity())

#OOP Exercise 5: Define a property that must have the same value for every class instance (object)

class Vehicle:
    # Class attribute
    color = "White"

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

School_bus = Bus("School Volvo", 180, 12)
print(School_bus.color, School_bus.name, "Speed:", School_bus.max_speed, "Mileage:", School_bus.mileage)

car = Car("Audi Q5", 240, 18)
print(car.color, car.name, "Speed:", car.max_speed, "Mileage:", car.mileage)


    
#OOP Exercise 6: Class Inheritance

class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    def fare(self):
        total = super().fare()
        total = total + total*0.1
        return total

School_bus = Bus("School Volvo", 12, 50)
print("Total Bus fare is:", School_bus.fare())

#OOP Exercise 7: Check type of an object

class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo", 12, 50)
vehicle = Vehicle("hola", 12, 50)
print(type(School_bus))
print(type(vehicle))

#OOP Exercise 8: Determine if School_bus is also an instance of the Vehicle class

class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo", 12, 50)
print(isinstance(School_bus, Vehicle))









































#