from fastapi import FastAPI

from user import user

app = FastAPI()

p = user()#("claire", "cah365@pitt.edu", "food")

@app.get("/")
async def root():
    print("hello!", p.get_name())
    name = p.get_name()

    return menu

    return {"message": f"Hello World {name}"}


# class pastOrders(BaseModel):
#     Buisness: 
#     Date_Time: datetime
#     Price: int

# class Buisness(BaseModel):
#     Name: int
#     Category: 
#     Menu: 
#     Rating: int
#     Reviews: 
#     location:str
#     Bio: str

#     def hello(self):
#         print(hello)

# @app.post('/users')
# async def create_user(user: User):
#     return {'message': f'User {user.name} created successfully!'}