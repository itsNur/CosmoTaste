# CosmoTaste 🍽️🌌

A simple recipe manager API built with Flask.

## Features

- Add, view, update, and delete recipes
- JSON file used as simple database (for learning purposes)
- Modular project structure

## API Endpoints

### GET /recipes
Returns a list of all recipes.

### POST /recipes
Add a new recipe.

### GET /recipes/<id>
Returns a specific recipe by ID.

### PUT /recipes/<id>
Update a specific recipe.

### DELETE /recipes/<id>
Deletes a recipe.

## Setup
- git clone https://github.com/itsNur/cosmotaste.git
- cd cosmotaste
- pip install -r requirements.txt
- python run.py
