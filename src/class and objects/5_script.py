# Example

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, My name is {self.name} and I am {self.age} years old.")

person = Person("John Wick", 40)
person.greet()