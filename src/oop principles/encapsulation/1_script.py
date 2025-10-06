# Encapsulation in Python
# # Encapsulation is one of the four fundamental OOP concepts.
# # It describes the idea of bundling data and methods that work on that data within one unit, e.g., a class in Python.
# # This concept is used to restrict direct access to some of an object's components, which can prevent the accidental modification of data. To achieve this, Python uses access modifiers.

# Without Encapsulation
class BadBankAccount:
    def __init__(self, balance):
        self.balance = balance

account1 = BadBankAccount(0.0)
account1.balance = -1  # Directly modifying the balance
print(account1.balance)

# No control over how balance is modified, which can lead to invalid states (like negative balance).