from fastapi import FastAPI

from user import user

app = FastAPI()

p = user("claire", "cah365@pitt.edu", "food", "6969")

from Food import food_list
from business import business
from Review import review_list

b = business("Grandma's edibles", "Dessert", review_list, 0, "15min", "pitt", "brownies")
b.avg_stars = b.get_avg_stars(review_list)





@app.get("/")
async def root():
    print("hello!", p.get_name())
    name = p.get_name()
    #return b.avg_stars
    return b.get_reviews()
    #return review_list
    #return food_list




# @app.post('/users')
# async def create_user(user: User):
#     return {'message': f'User {user.name} created successfully!'}
