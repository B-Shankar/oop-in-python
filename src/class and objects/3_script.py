# Create a Dog class with attributes name, breed, and owner (which is an instance of the Owner class). The Owner class should have attributes name, address, and contact_number.
# Implement a method bark in the Dog class that prints "Whoof Whoof".
# Create instances of both classes and demonstrate accessing the owner's name through the Dog instance.

class Dog:
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner

    def bark(self):
        print("Whoof Whoof")

class Owner:
    def __init__ (self, name, address, contact_number):
        self.name = name
        self.address = address
        self.mobile_number = contact_number


owner1 = Owner("Joy", "123 Street Avenue", "123-456-7890")
dog1 = Dog("Bruce", "Scottish Terrier", owner1)

owner2 = Owner("Jolly", "123 Main Avenue", "123-654-7890")
dog2 = Dog("Trolly", "Greyhound", owner2)

print("Dog Name:", dog1.name)
print("Breed:", dog1.breed)
print("Owner name:", dog1.owner.name)
dog1.bark()