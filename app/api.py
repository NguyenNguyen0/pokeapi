import requests
from app.constants import BASE_URL, POKEMON_PER_PAGE


def get_pokemons(offset=0, limit=POKEMON_PER_PAGE):
    pokemons = []
    for index in range(offset + 1, offset + limit + 1):
        pokemon = requests.get(f"{BASE_URL}/{index}").json()
        pokemon["image_url"] = pokemon["sprites"]["front_default"]
        pokemon["types"] = [t["type"]["name"] for t in pokemon["types"]]
        pokemons.append(pokemon)

    return pokemons
