import requests
import json
from flask import Flask, render_template

app = Flask(__name__)

BASE_URL = r"https://pokeapi.co/api/v2/pokemon"


@app.route("/")
def index():
    responses = requests.get(f"{BASE_URL}?offset=9&limit=9")
    pokemons = responses.json().get("results", [])
    for pokemon in pokemons:
        pokemon_details = requests.get(pokemon["url"]).json()
        pokemon["image_url"] = pokemon_details["sprites"]["front_default"]
        pokemon["types"] = [t["type"]["name"] for t in pokemon_details["types"]]
        pokemon["id"] = pokemon_details["id"]

    return render_template("index.html", pokemons=pokemons)


if __name__ == "__main__":
    app.run(debug=True)
