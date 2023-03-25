from fastapi import FastAPI
from pydantic import BaseModel
import datetime
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


class User(BaseModel):
    name: str
    email: str
    age: int
    Subscription: 

class pastOrders(BaseModel):
    Buisness: 
    Date_Time: datetime
    Price: int

class Buisness(BaseModel):
    Name: int
    Category: 
    Menu: 
    Rating: int
    Reviews: 
    location:str
    Bio: str

    def hello(self):
        print(hello)


@app.post('/users')
async def create_user(user: User):
    return {'message': f'User {user.name} created successfully!'}