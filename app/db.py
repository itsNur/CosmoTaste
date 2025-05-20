import os

import psycopg2
from psycopg2.extras import RealDictCursor


def get_connection():
    database_url = os.getenv('DATABASE_URL')

    if not database_url:
        raise ValueError('DATABASE_URL environment variable not set. Please check your .env file.')

    return psycopg2.connect(database_url)

def get_all_recipes():
    recipes = []

    with get_connection() as conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cursor:
            try:
                cursor.execute('SELECT * FROM recipes')
                recipes = cursor.fetchall()
            except psycopg2.Error as e:
                print(f'Database error in get_all_recipes: {e}')
                raise  # Re-raise for handling in routes.py
    return recipes

def add_recipes_to_db(title, ingredients, instructions):
    new_recipe = None

    with get_connection() as conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cursor:
            try:
                cursor.execute(
                    '''
                    INSERT INTO recipes (title, ingredients, instructions)
                    VALUES (%s, %s, %s)
                    RETURNING *;
                    ''',
                    (title, ingredients, instructions)
                )
                new_recipe = cursor.fetchone()
                conn.commit() # Commit changes here, as it's an INSERT
            except psycopg2.Error as e:
                print(f'Database error in add_recipes_to_db: {e}')
                conn.rollback() # Rollback changes if an error occurs during commit
                raise # Re-raise for handling in routes.py
    return new_recipe

def get_recipe_by_id_from_db(recipe_id):
    recipe = None

    with get_connection() as conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cursor:
            try:
                cursor.execute(
                    '''
                    SELECT *
                    FROM recipes
                    WHERE id = %s
                    ''',
                    (recipe_id,)
                )
                recipe = cursor.fetchone()
            except psycopg2.Error as e:
                print(f'Database error in get_recipe_by_id_from_db: {e}')
                raise # Re-raise the exception to be handled by the caller (routes.py)
    return recipe
