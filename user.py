
class user:
    def __init__(self, name, email, subscription, cardNum):
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

    def get_cardNum(self):
        return self._cardNum

    def set_cardNum(self, cardNum):
        self._cardNum = cardNum
