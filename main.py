from app import app
from flask import jsonify, render_template
from app.api import get_pokemons
from app.constants import POKEMON_PER_PAGE

@app.route("/")
def index():
    pokemons = get_pokemons()
    return render_template("index.html", pokemons=pokemons)


@app.route("/pokemons/<int:page>")
def get_pokemons_by_page(page):
    offset = (page - 1) * POKEMON_PER_PAGE
    pokemons = get_pokemons(offset=offset)
    return jsonify(pokemons)


if __name__ == "__main__":
    app.run(debug=True)
