# Class with constructor(Initializer) and method

class Dog:
    # Constructor or Initializer: __init__ special method, that is called only when an object is created from a class.
    # self refers to the instance of the class and objects on which the method is being called. It allows you to access and manipulate the instance's attributes (variables) and methods within the class and objects.
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print("whoof whoof")


dog_test = Dog("Bruce", "Scottish Terrier")
dog_test.bark()
print(dog_test.name)
print(dog_test.breed)