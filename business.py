from Review import Review

class business:
    def __init__(self, name, category, reviews, avgStars, avalibility, location, bio):
        self._name = name #buisness name
        self._category = category #kind of food or buisness
        self._reviews = reviews#reviewli
        self._avgStars = avgStars
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

    def get_reviews(self):
        return self._reviews

    def set_reviews(self, reviews):
        self._reviews = reviews

    def get_avg_stars(self, reviews):
        stars = [review.get_stars() for review in reviews]
        avg_stars = sum(stars) / len(stars)
        return avg_stars

    def get__avalibility(self):
        return self._avalibility

    def set_avalibility(self, avalibility):
        self._avalibility = avalibility

    def get__bio(self):
        return self._bio

    def set_bio(self, bio):
        self._bio = bio