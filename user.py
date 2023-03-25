
class User:
    def __init__(self, name, email, subscription):
        self._name = name
        self._email = email
        self._subscription = subscription
    
    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_email(self):
        return self._email

    def set_email(self, email):
        self._email = email

    def get_subscription(self):
        return self._subscription

    def set_subscription(self, subscription):
        self._subscription = subscription

