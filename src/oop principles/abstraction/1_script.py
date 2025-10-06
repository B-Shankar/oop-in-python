# Abstraction in OOP
# Abstraction is one of the four fundamental OOP concepts.
# It involves hiding complex implementation details and showing only the essential features of the object.
# This helps in reducing complexity and increases efficiency.

class EmailService:

    def connect(self): # Protected Method
        print("Connecting to email server...")

    def authenticate(self): # Protected Method
        print("Authenticating...")

    def disconnect(self): # Protected Method
        print("Disconnecting...")

    def send_email(self): # Public Method
        print("Sending email...")


email_service = EmailService()
email_service.connect()
email_service.authenticate()
email_service.send_email()
email_service.disconnect()

# Here, user is exposed unnecessary tasks like connect, authenticate, disconnect. With Abstraction, we can hide this complexity.