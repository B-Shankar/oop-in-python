# Polymorphism

# The Word polymorphism is derived from Greek, and means "having multiple forms":
# Poly = many; morph = form.


class Car:
    def __init__(self, brand, model, year, number_of_doors, number_of_wheels):
        self.brand = brand
        self.model = model
        self.year = year
        self.number_of_doors = number_of_doors
        self.number_of_wheels = number_of_wheels

    def start(self):
        print(f"The car is starting.")

    def stop(self):
        print(f"The car is stopped.")


class MotorCycle:
    def __init__(self, brand, model, year, number_of_wheels):
        self.brand = brand
        self.model = model
        self.year = year
        self.number_of_wheels = number_of_wheels

    def start_bike(self):
        print("The bike is starting.")

    def stop_bike(self):
        print("The bike is stopped.")


# Create list of vehicles
vehicles = [
    Car("BMW", "X5", 2020, 4, 4),
    MotorCycle("Harley-Davidson", "Street 750", 2019, 2)
]

# Loop through list of vehicles and inspect them
for vehicle in vehicles:
    if isinstance(vehicle, Car):
        print(f"Inspecting {vehicle.brand} {vehicle.model} ({type(vehicles).__name__})")
        vehicle.start()
        vehicle.stop()
    elif isinstance(vehicle, MotorCycle):
        print(f"Inspecting {vehicle.brand} {vehicle.model} ({type(vehicles).__name__})")
        vehicle.start_bike()
        vehicle.stop_bike()
    else:
        raise Exception("Object is not a valid vehicle.")


# Here, if we introduce a new vehicle type, we would have to modify the code in the loop.
# This violates the Open/Closed Principle, which states that software entities should be open for extension but closed for modification.
# To adhere to this principle, we can use polymorphism by defining a common interface for all