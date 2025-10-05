# Modifying object data

class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email =email
        self.password = password

    def say_hi_to_user(self, user):
        print(f"Sending message to {user.username}: Hi {user.username}, it's {self.username}")

user1 = User("John Wick", "john@gmail.com", "12345")

print("Before:", user1.email)

user1.email = "john.wick@gamil.com"

print("After:",user1.email)

# Issue: there is no control on accessing and modifying data. So we will use Access Modifiers