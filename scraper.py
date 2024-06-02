import requests
import urllib.request

from bs4 import BeautifulSoup


url = 'https://www.bbcgoodfood.com/recipes/oven-baked-risotto'

#input("Choose a recipe url: ")

recipeUrl = f"https://cooked.wiki/{url}"

s = requests.session() 
response = s.get(recipeUrl) 

response = response.content

soup = BeautifulSoup(response, 'html.parser')

ingredientList = soup.find('div', class_='shopping-list')

ingredients = ingredientList.findAll('li', class_='ingredient')

for item in ingredients:
    box = item.find('label')
    ingredient = box.find('input')
    ing = ingredient.attrs['value']

    print(ing)


