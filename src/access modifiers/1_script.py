# SOLUTION: we need a way of controlling the way we can get and set data. Let me show you two ways: one traditional "Java"-style, and one the more modern "Python" (and C#) style.

# 1. The traditional way: make the data private and use getters and setters:

# Mangling: Python does not have true private attributes, but it has a way of "mangling" the names of attributes that start with double underscores (__). This makes it harder (but not impossible) to access them from outside the class.

class User:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email # protected attribute: if it with prefix _, it means "please don't access it directly"
        self.__password = password # private attribute: if it with prefix __, it means "don't access it directly, even in subclasses"
        self.password = password # public attribute: anyone can access it

    def clean_email(self):
        return self._email.lower().strip()

user1 = User("John Wick", " john@gmail.com   ", "12345")

print(user1._email) # accessing protected attribute directly (not recommended, but possible)
print(user1.clean_email())


# "The Consenting Adults" Philosophy

# The consenting adults approach: we can access the protected attribute directly, but we should know what we are doing.
