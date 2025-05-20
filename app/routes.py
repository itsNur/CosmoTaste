from flask import request, jsonify, Blueprint
from app.db import get_all_recipes, add_recipes_to_db


bp = Blueprint('routes', __name__)


@bp.route('/recipes', methods=['GET'])
def get_recipes():
    try:
        recipes = get_all_recipes()
        return jsonify(recipes)
    except Exception as e:
        # Log the error for debugging, then return a generic error to the client
        print(f'Error fetching recipes: {e}')
        return jsonify({'error': 'Could not retrieve recipes from the database.'}), 500

@bp.route('/recipes', methods=['POST'])
def add_recipe():
    data = request.get_json()

    if 'title' not in data or 'ingredients' not in data or 'instructions' not in data:
        return jsonify({'error': 'Missing fields'}), 400

    try:
        new_recipe = add_recipes_to_db(
            data['title'],
            data['ingredients'],
            data['instructions']
        )
        # Ensure new_recipe is not None (in case db function fails to return a recipe)
        if new_recipe:
            return jsonify(new_recipe), 201
        else:
            return jsonify({'error': 'Failed to add recipe to database.'}), 500
    except Exception as e:
        print(f"Error adding recipe: {e}")
        return jsonify({'error': 'Could not save recipe to the database.'}), 500
