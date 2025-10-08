# Inheritance

#  Inheritance is the fundamental principle of object-oriented programming (OOP) that involves creating new classes (subclasses or derived classes) based on existing classes (superclasses or base classes).
# A Car is a Vehicle
# A Bike is a Vehicle

class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        print("Vehicle is starting...")

    def stop(self):
        print("Vehicle is stopping...")


class Car(Vehicle):
    def __init__(self, brand, model, year, number_of_doors, number_of_wheels):
        super().__init__(brand, model, year)
        self.number_of_doors = number_of_doors
        self.number_of_wheels = number_of_wheels

class Bike(Vehicle):
    def __init__(self, brand, model, year, number_of_wheels):
        super().__init__(brand, model, year)
        self.number_of_wheels = number_of_wheels


car = Car("BMW", "X5", 2020, 4, 4)
bike = Bike("Harley-Davidson", "Street 750", 2019, 2)

print(car.__dict__) # {'brand': 'BMW', 'model': 'X5', 'year': 2020, 'number_of_doors': 4, 'number_of_wheels': 4}
print(bike.__dict__) # {'brand': 'Harley-Davidson', 'model': 'Street 750', 'year': 2019, 'number_of_wheels': 2}
car.start()
bike.stop()