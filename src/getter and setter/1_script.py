# Getter and Setter: Full control over attribute access and modification
# This java-style approach of using getters and setters

from datetime import datetime

class User:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email # protected attribute: if it with prefix _, it means "please don't access it directly"
        self.__password = password # private attribute: if it with prefix __, it means "don't access it directly, even in subclasses"
        self.password = password # public attribute: anyone can access it

    def get_email(self):
        print(f"------Email Accessed at {datetime.now()}------")
        return self._email

    def set_email(self, new_email):
        if "@" in new_email:
            self._email = new_email
            print(f"------Email Modified at {datetime.now()}------")

user1 = User("John Wick", "john@gmail.com", "12345")

print("Email Before:",user1.get_email())
user1.set_email("john.wick@gmail.com")  # valid email
print("Email After:",user1.get_email())