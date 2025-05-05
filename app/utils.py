import json
import os.path


DATA_FILE = 'app/recipes.json'

# Function: load recipes from file
def load_recipes():
    if not os.path.exists(DATA_FILE) or os.path.getsize(DATA_FILE) == 0:
        return []
    with open(DATA_FILE, 'r', encoding='utf-8') as file:
        return json.load(file)


# Function: save recipes to the file:
def save_recipes(recipes):
    with open(DATA_FILE, 'w', encoding='utf-8') as file:
        json.dump(recipes, file, indent=4)