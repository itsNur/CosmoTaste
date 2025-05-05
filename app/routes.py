from flask import request, jsonify
from app import app
from app.utils import load_recipes, save_recipes


@app.route('/recipes', methods=['GET'])
def get_recipes():
    """Get all recipes"""
    recipes = load_recipes()
    return jsonify(recipes)


@app.route('/recipes', methods=['POST'])
def add_recipe():
    """Add new recipe"""
    data = request.get_json()
    recipes = load_recipes()

    if 'title' not in data or 'ingredients' not in data or 'instructions' not in data:
        return jsonify({'error': 'Missing fields'}), 400

    new_recipe = {
        'id': len(recipes) + 1,
        'title': data['title'],
        'ingredients': data['ingredients'],
        'instructions': data['instructions']
    }

    recipes.append(new_recipe)
    save_recipes(recipes)
    return jsonify(new_recipe), 201


@app.route('/recipes/<int:recipe_id>', methods=['GET'])
def get_recipe(recipe_id):
    """Get recipe by id"""
    recipes = load_recipes()
    for recipe in recipes:
        if recipe['id'] == recipe_id:
            return jsonify(recipe)
    return jsonify({'error': 'Recipe not found'}), 404


@app.route('/recipes/<int:recipe_id>', methods=['DELETE'])
def delete_recipe(recipe_id):
    """Delete recipe by id"""
    recipes = load_recipes()
    updated_recipes = [r for r in recipes if r['id'] != recipe_id]

    if len(updated_recipes) == len(recipes):
        return jsonify({'error': 'Recipe not found'}), 404

    save_recipes(updated_recipes)
    return jsonify({'message': 'Recipe deleted'}), 200


@app.route('/recipes/<int:recipe_id>', methods=['PUT'])
def update_recipe(recipe_id):
    """Update recipe by id"""
    recipes = load_recipes()
    data = request.get_json()

    if 'title' not in data or 'ingredients' not in data or 'instructions' not in data:
        return jsonify({'error': 'Missing fields'}), 400

    for recipe in recipes:
        if recipe['id'] == recipe_id:
            recipe['title'] = data['title']
            recipe['ingredients'] = data['ingredients']
            recipe['instructions'] = data['instructions']
            save_recipes(recipes)
            return jsonify(recipe), 200

    return jsonify({'error': 'Recipe not found'}), 404
