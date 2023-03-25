from business import business

class subscription:
    def __init__(self, business, date, time, food, user):
        self._business = business
        self._date = date
        self._time = time
        self._food = food
        self._user = user
    
    def get_business(self):
        return self._business

    def set_business(self, bus):
        self._business = bus
    
    def get_date(self):
        return self._date

    def set_date(self, date):
        self._date = date

    def get_time(self):
        return self._time
    
    def set_time(self, time):
        self._time = time
    
    def get_food(self):
        return self._food

    def set_food(self, food):
        self._food = food

    def get_user(self):
        return self._user

    def set_user(self, user):
        self._user = user

