# CosmoTaste 🍽️🌌

A versatile recipe manager API built with Flask.

## Features

- Add, view, update, and delete recipes
- Persistent data storage using PostgreSQL
- Modular project structure with Flask Blueprints

## API Endpoints

* **GET /recipes**
    * Returns a list of all recipes.

* **POST /recipes**
    Adds a new recipe.
    * **Request Body:** `{"title": "string", "ingredients": "string", "instructions": "string"}`

* **GET /recipes/<int:recipe_id>**
    Returns a specific recipe by its unique ID.
    * **Example:** `/recipes/1`

* **PUT /recipes/<int:recipe_id>** (Placeholder for future)
    Updates an existing recipe by its ID.

* **DELETE /recipes/<int:recipe_id>** (Placeholder for future)
    Deletes a recipe by its ID.

## Setup
1.  **Clone the repository:**
    ```bash
    git clone https://github.com/itsNur/cosmotaste.git
    cd cosmotaste
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Set up PostgreSQL Database:**
    * Ensure you have **PostgreSQL** installed and running on your system.
    * Create a new database (e.g., `cosmotaste`).
        * Example using `psql` command line: `CREATE DATABASE cosmotaste;`
    * Set up a user with appropriate permissions if needed (e.g., `CREATE USER myuser WITH PASSWORD 'mypassword'; GRANT ALL PRIVILEGES ON DATABASE cosmotaste TO myuser;`).
    * Create the `recipes` table in your `cosmotaste` database:
        ```sql
        CREATE TABLE recipes (
            id SERIAL PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            ingredients TEXT NOT NULL,
            instructions TEXT NOT NULL
        );
        ```

4.  **Configure Environment Variables:**
    * Create a `.env` file in the root directory of your project.
    * Add your PostgreSQL connection string to it:
        ```
        DATABASE_URL="postgresql://<your_username>:<your_password>@<your_host>:<your_port>/<your_database_name>"
        # Example for local setup:
        # DATABASE_URL="postgresql://postgres:mysecretpassword@localhost:5432/cosmotaste"
        ```

5.  **Run the application:**
    ```bash
    python run.py
    ```
    The API will be available at `http://127.0.0.1:5000`.
