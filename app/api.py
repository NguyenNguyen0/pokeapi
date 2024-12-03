import requests
from app.constants import POKEMON_DETAIL_URL, POKEMON_PER_PAGE


def get_pokemons(offset=0, limit=POKEMON_PER_PAGE):
    if offset < 0:
        offset = 0
    else:
        offset = offset

    pokemons = []
    for index in range(offset + 1, offset + limit + 1):
        pokemon = requests.get(f"{POKEMON_DETAIL_URL}/{index}").json()
        pokemon["image_url"] = pokemon["sprites"]["front_default"]
        pokemon["types"] = [t["type"]["name"] for t in pokemon["types"]]
        pokemons.append(pokemon)

    return pokemons


def get_pokemons_by_page(page):
    offset = (page - 1) * POKEMON_PER_PAGE
    pokemons = get_pokemons(offset=offset)
    next = f"/api/pokemons/{page + 1}"
    previous = f"/api/pokemons/{page - 1}" if page > 1 else None
    return {"page": page, "next": next, "previous": previous, "pokemons": pokemons}
