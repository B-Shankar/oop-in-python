# Getter and Setter: Full control over attribute access and modification
# This is using Property Decorators: Pythonic way of using getters and setters

from datetime import datetime

class User:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email
        self.__password = password
        self.password = password

    # Getter
    @property
    def email(self):
        print(f"------Email Accessed at {datetime.now()}------")
        return self._email

    # Setter
    @email.setter
    def email(self, new_email):
        if "@" in new_email:
            self._email = new_email
            print(f"------Email Modified at {datetime.now()}------")
        else:
            print("Invalid email format. Email not updated.")

user1 = User("John Wick", "john@gmail.com", "12345")

print(user1.email) # accessing email using the getter
user1.email = "john.wick@gmail.com"  # valid email, using the setter
print(user1.email)
