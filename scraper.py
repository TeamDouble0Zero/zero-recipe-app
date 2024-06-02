import requests
import urllib.request

from bs4 import BeautifulSoup


url = 'https://www.bbcgoodfood.com/recipes/oven-baked-risotto'

recipeUrl = f"https://cooked.wiki/{url}"

s = requests.session() 
response = s.get(recipeUrl) 

response = response.content

soup = BeautifulSoup(response, 'html.parser')

ingredients = soup.findAll(name='ingredients')

print(ingredients.value)


