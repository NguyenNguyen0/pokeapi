## Description
**Simple python flask project with pokeapi**


## Installation

1. **Clone the repository**:
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Create a virtual environment**:
    ```sh
    python -m venv venv
    ```

3. **Activate the virtual environment**:
    - On Windows:
        ```sh
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source venv/bin/activate
        ```

4. **Install the dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

## Running the Application

1. **Run the Flask application**:
    ```sh
    python main.py
    ```

2. **Open your web browser** and navigate to `http://127.0.0.1:5000/`.

## Project Files

- **`main.py`**: The main entry point of the application.
- **[app/__init__.py](http://_vscodecontentref_/6)**: Initializes the Flask application.
- **[app/api.py](http://_vscodecontentref_/7)**: Contains functions to fetch Pokémon data from the PokeAPI.
- **[app/constants.py](http://_vscodecontentref_/8)**: Contains constants used in the application.
- **[app/templates/index.html](http://_vscodecontentref_/9)**: The main HTML template for the application.
- **[static](http://_vscodecontentref_/10)**: Contains static files (CSS, JavaScript, images).

## API Endpoints

- **`GET /`**: Renders the main page with a list of Pokémon.
- **`GET /api/pokemons/<int:page>`**: Returns a JSON response with Pokémon data for the specified page.
- **`GET /api/pokemons/<name>`**: Returns a JSON response with data for the specified Pokémon.

## License

This project is licensed under the MIT License.

