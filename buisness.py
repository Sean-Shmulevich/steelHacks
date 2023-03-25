class buisness:
    def __init__(self, name, category, rating, avalibility, bio):
        self._name = name #buisness name
        self._category = category #kind of food or buisness
        self._rating = rating
        self._avalibility = avalibility #(est pickup time 17min)
        self._location = location #address
        self._bio = bio
        
    
    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_category(self):
        return self._category

    def set_category(self, category):
        self._category = category

    def get__rating(self):
        return self._rating

    def set_rating(self, rating):
        self._rating = rating

    def get__avalibility(self):
        return self._avalibility

    def set_avalibility(self, avalibility):
        self._avalibility = avalibility

    def get__bio(self):
        return self._bio

    def set_bio(self, bio):
        self._bio = bio