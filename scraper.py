import requests
import urllib.request

from bs4 import BeautifulSoup

#Asks user for URL for recipe and converts it
url = input("Choose a recipe url: ")
recipeUrl = f"https://cooked.wiki/{url}"

#This stage allows the conversion redirect to happen
s = requests.session() 
response = s.get(recipeUrl) 
response = response.content

#Retrieves the HTML
soup = BeautifulSoup(response, 'html.parser')


#This finds the ingredient list and prints to the terminal
def retrieveIngredients():
    ingredientList = soup.find('div', class_='shopping-list')
    ingredients = ingredientList.findAll('li', class_='ingredient')

    for item in ingredients:
        box = item.find('label')
        ingredient = box.find('input')
        ing = ingredient.attrs['value']

        print(ing)

#Finds and prints recipe title
def retrieveTitle ():
    titleBox = soup.find('div', class_='title')
    title = titleBox.text

    print(title)


#Finds the instructions, adds a step number, then prints result
def retrieveInstructions():
    lineNumber = 0
    instructionPage = soup.find('div', class_='recipe-content')
    instructionBox = instructionPage.find('ol')
    instructions = instructionBox.findAll('li')

    for item in instructions:
        lines = item.find('p')
        instruction = lines.text
        lineNumber=lineNumber+1
        print(str(lineNumber)+'.'+instruction)




retrieveTitle ()
retrieveIngredients()
retrieveInstructions()
