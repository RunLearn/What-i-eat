import requests

def get_foodname():
    resp = requests.get('https://www.themealdb.com/api/json/v1/1/random.php')
    food_name = resp.json()["meals"][0]["strMeal"]
    return food_name

