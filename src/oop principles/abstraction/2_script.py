# With Abstraction

class EmailService:

    def _connect(self): # Protected Method
        print("Connecting to email server...")

    def _authenticate(self): # Protected Method
        print("Authenticating...")

    def _disconnect(self): # Protected Method
        print("Disconnecting...")

    def send_email(self): # Public Method
        self._connect()
        self._authenticate()
        print("Sending email...")
        self._disconnect()

# Not to any Protected or Private methods
email_service = EmailService()
email_service.send_email()