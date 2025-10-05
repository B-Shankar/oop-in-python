# Static Attributes

# A static attribute (sometimes called a class attribute) ia an attribute that belongs to the class itself, rather than to any specific instance of the class.
# or
# A static attribute (sometimes called a class attribute) is an attribute that is shared by all instances of a class. It is defined within the class but outside any instance methods. Static attributes are used to store data that is common to all instances of the class.

class User:
    user_count = 0  # static attribute to keep track of the number of users

    def __init__(self, username, email):
        self.username = username
        self.email = email
        User.user_count += 1  # increment the user count when a new user is created

    def display_user(self):
        print(f"Username: {self.username}, Email: {self.email}")

# Creating instances of the User class
user1 = User("@alice_specter", "alice.s@gmail.com")
user2 = User("@bob_builder", "bob.builder@gmail.com")

# Accessing the static attribute
print("Total Users:", User.user_count)  # Output: Total Users: 2

print(user1.user_count) # 2
print(user2.user_count) # 2

# Static attributes used to keep track of data that is common to all instances of the class. Like total, count, default value that same in all instances(like fixed size), etc.