# Overriding methods in derived classes
# vehicle types. This way, we can add new vehicle types without changing the existing code.
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

    def start(self):
        print(f"The car is starting.")

    def stop(self):
        print(f"The car is stopped.")

class MotorCycle(Vehicle):
    def __init__(self, brand, model, year, number_of_wheels):
        super().__init__(brand, model, year)
        self.number_of_wheels = number_of_wheels

    def start(self):
        print(f"The MotorCycle is starting.")

    def stop(self):
        print(f"The MotorCycle is stopped.")

class Plane(Vehicle):
    def __init__(self, brand, model, year, number_of_wheels):
        super().__init__(brand, model, year)
        self.number_of_wheels = number_of_wheels

    def start(self):
        print(f"The Plane is starting.")

    def stop(self):
        print(f"The Plane is stopped.")

# Create list of vehicles
vehicles: list[Vehicle] = [
    Car("BMW", "X5", 2020, 4, 4),
    MotorCycle("Harley-Davidson", "Street 750", 2019, 2),
    Plane("Boeing", "747", 2015, 18)
]

# Loop through list of vehicles and inspect them
for vehicle in vehicles:
    print(f"------Inspecting {vehicle.brand} {vehicle.model} ({type(vehicles).__name__})------")
    vehicle.start()
    vehicle.stop()
