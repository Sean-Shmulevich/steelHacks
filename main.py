from fastapi import FastAPI
from user import user

app = FastAPI()

p = user("claire", "cah365@pitt.edu", "food", "6969")

from Food import food_list
from business import business
from Review import review_list
from pastOrders import orders_list



@app.get("/Home/") #main page
async def root0():
    return business_list

@app.get("/bus/") #Buisness pages
async def root1(b_id: int):
    return business_list[b_id]
    #return b_id.get_reviews()
    #return review_list
    #return food_list

@app.get("/bus/orders/{num}") #orders page
async def root1(num):
    return orders_list




# create 40 instances of the business class and assign them to variables
b1 = business("Grandma's edibles", "Dessert", [], 0, "15min", "pitt", "fun desserts and yummy stuff") #B1 will be only REAL business with menu and reviews and stars
b1.avg_stars = b1.get_avg_stars(review_list)
b2 = business("Tom's Tacos", "Mexican", [], 0, "20min", "New York City", "authentic Mexican food")
b2.avg_stars = b2.get_avg_stars(review_list)
b3 = business("Farmer John", "Produce", [], 0, "10min", "Ohio", "Eggs and lettuce")
b3.avg_stars = b3.get_avg_stars(review_list)
b4 = business("Mama's Kitchen", "Family Style", [], 0, "25min", "Atlanta", "homestyle cooking")
b4.avg_stars = b4.get_avg_stars(review_list)
b5 = business("Bob's Burgers", "American", [], 0, "10min", "Los Angeles", "classic burgers and fries")
b5.avg_stars = b5.get_avg_stars(review_list)
b6 = business("Pizza Palace", "Italian", [], 0, "30min", "Chicago", "authentic pizza")
b6.avg_stars = b6.get_avg_stars(review_list)
b7 = business("Sushi Sam", "Japanese", [], 0, "20min", "San Francisco", "fresh sushi")
b7.avg_stars = b7.get_avg_stars(review_list)
b8 = business("Thai House", "Thai", [], 0, "25min", "Boston", "spicy curries")
b8.avg_stars = b8.get_avg_stars(review_list)
b9 = business("Peking Palace", "Chinese", [], 0, "15min", "New York City", "traditional Chinese food")
b9.avg_stars = b9.get_avg_stars(review_list)
b10 = business("Taco Tuesday", "Mexican", [], 0, "15min", "Austin", "tacos and margaritas")
b10.avg_stars = b10.get_avg_stars(review_list)
b11 = business("Pho King", "Vietnamese", [], 0, "25min", "Seattle", "hearty pho bowls")
b11.avg_stars = b11.get_avg_stars(review_list)
b12 = business("The Grill House", "Steakhouse", [], 0, "30min", "Las Vegas", "prime cuts of beef")
b12.avg_stars = b12.get_avg_stars(review_list)
b13 = business("Soup and Salad", "Healthy", [], 0, "10min", "Miami", "fresh salads and soups")
b13.avg_stars = b13.get_avg_stars(review_list)
b14 = business("Burger Bar", "American", [], 0, "20min", "New York City", "gourmet burgers")
b14.avg_stars = b14.get_avg_stars(review_list)
b15 = business("Taste of India", "Indian", [], 0, "30min", "San Francisco", "spicy curries and naan bread")
b15.avg_stars = b15.get_avg_stars(review_list)
b16 = business("Fish and Chips", "British", [], 0, "25min", "Los Angeles", "classic fish and chips")
b16.avg_stars = b16.get_avg_stars(review_list)
b17 = business("La Taqueria", "Mexican", [], 0, "15min", "Chicago", "authentic Mexican food")
b17.avg_stars = b17.get_avg_stars(review_list)
b18 = business("The Waffle House", "Breakfast", [], 0, "20min", "Atlanta", "fluffy waffles")
b18.avg_stars = b18.get_avg_stars(review_list)
b19 = business("Soul Food Cafe", "Soul Food", [], 0, "30min", "New Orleans", "fried chicken and collard greens")
b19.avg_stars = b19.get_avg_stars(review_list)
b20 = business("Falafel King", "Middle Eastern", [], 0, "15min", "Boston", "fresh falafel")
b20.avg_stars = b20.get_avg_stars(review_list)
b21 = business("Tony's Pizza", "Italian", review_list, 0, "25min", "Chicago", "Classic pizza pies")
b21.avg_stars = b21.get_avg_stars(review_list)
b22 = business("Sushi Sama", "Japanese", review_list, 0, "30min", "Los Angeles", "Fresh sushi rolls")
b22.avg_stars = b22.get_avg_stars(review_list)
b23 = business("The Burger Joint", "American", review_list, 0, "15min", "Houston", "Juicy burgers and fries")
b23.avg_stars = b23.get_avg_stars(review_list)
b24 = business("Thai Spice", "Thai", review_list, 0, "20min", "Miami", "Authentic Thai dishes")
b24.avg_stars = b24.get_avg_stars(review_list)
b25 = business("La Taqueria", "Mexican", review_list, 0, "10min", "San Francisco", "Tasty tacos and burritos")
b25.avg_stars = b25.get_avg_stars(review_list)
b26 = business("Café Parisien", "French", review_list, 0, "30min", "Paris", "Croissants and coffee")
b26.avg_stars = b26.get_avg_stars(review_list)
b27 = business("The Indian Kitchen", "Indian", review_list, 0, "25min", "London", "Curries and naan bread")
b27.avg_stars = b27.get_avg_stars(review_list)
b28 = business("El Gran Sabor", "Venezuelan", review_list, 0, "20min", "Blacksburg", "Arepa sandwiches")
b28.avg_stars = b28.get_avg_stars(review_list)
b29 = business("The Fisherman's Catch", "Seafood", review_list, 0, "30min", "Sydney", "Fresh seafood dishes")
b29.avg_stars = b29.get_avg_stars(review_list)
b30 = business("BBQ Shack", "Barbecue", review_list, 0, "15min", "Austin", "Slow-cooked BBQ meats")
b30.avg_stars = b30.get_avg_stars(review_list)
b31 = business("The Veggie Patch", "Vegetarian", review_list, 0, "20min", "Portland", "Healthy vegetarian dishes")
b31.avg_stars = b31.get_avg_stars(review_list)
b32 = business("El Mexicano", "Mexican", review_list, 0, "10min", "Guadalajara", "Tacos and margaritas")
b32.avg_stars = b32.get_avg_stars(review_list)
b33 = business("Ramen Master", "Japanese", review_list, 0, "25min", "Tokyo", "Authentic ramen bowls")
b33.avg_stars = b33.get_avg_stars(review_list)
b34 = business("The Italian Job", "Italian", review_list, 0, "30min", "Rome", "Pasta and pizza dishes")
b34.avg_stars = b34.get_avg_stars(review_list)
b35 = business("Spice House", "Indian", review_list, 0, "20min", "Mumbai", "Spicy Indian dishes")
b35.avg_stars = b35.get_avg_stars(review_list)
b36 = business("Burger Boss", "American", review_list, 0, "15min", "New Orleans", "Gourmet burgers")
b36.avg_stars = b36.get_avg_stars(review_list)
b37 = business("Italian Bistro", "Italian", [], 0, "25min", "Seattle", "pasta and meat dishes")
b37.avg_stars = b37.get_avg_stars(review_list)
b38 = business("Mama's Pizza", "Italian", review_list, 0, "30min", "Chicago", "homemade pizza")
b38.avg_stars = b38.get_avg_stars(review_list)
b39 = business("Green Garden", "Vegetarian", review_list, 0, "15min", "San Francisco", "organic veggies and salads")
b39.avg_stars = b39.get_avg_stars(review_list)
b40 = business("The Burger Joint", "American", review_list, 0, "25min", "Los Angeles", "classic burgers and fries")
b40.avg_stars = b40.get_avg_stars(review_list)

business_list = [b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16, b17, b18, b19, b20, b21, b22, b23, b24, b25, b26, b27, b28, b29, b30, b31, b32, b33, b34, b35, b36, b37, b38, b39, b40]
