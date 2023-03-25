from fastapi import FastAPI

import user

app = FastAPI()

p = user("c", "h", "c")

@app.get("/")
async def root():
    print(p.get_name(p))
    return {"message": "Hello World"}


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