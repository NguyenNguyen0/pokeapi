import requests
import aiohttp
import asyncio

from app.constants import POKEMON_DETAIL_URL, POKEMON_PER_PAGE


def get_pokemon_by_name(name):
    pokemon = requests.get(f"{POKEMON_DETAIL_URL}/{name}").json()
    pokemon["image_url"] = pokemon["sprites"]["front_default"]
    pokemon["types"] = [t["type"]["name"] for t in pokemon["types"]]
    for index, stat in enumerate([
        "hp",
        "attack",
        "defense",
        "special_attack",
        "special_defense",
        "speed",
    ]):
        pokemon[stat] = pokemon["stats"][index]["base_stat"] 
    return pokemon


def get_pokemons_by_page(page):
    offset = (page - 1) * POKEMON_PER_PAGE
    pokemons = asyncio.run(get_pokemons_async(offset=offset))
    next = f"/api/pokemons/{page + 1}"
    previous = f"/api/pokemons/{page - 1}" if page > 1 else None
    return {"page": page, "next": next, "previous": previous, "pokemons": pokemons}


async def fetch_pokemon(session, index):
    async with session.get(f"{POKEMON_DETAIL_URL}/{index}") as response:
        pokemon = await response.json()
        pokemon["image_url"] = pokemon["sprites"]["front_default"]
        pokemon["types"] = [t["type"]["name"] for t in pokemon["types"]]
        return pokemon


async def get_pokemons_async(offset=0, limit=POKEMON_PER_PAGE):
    if offset < 0:
        offset = 0
    else:
        offset = offset

    async with aiohttp.ClientSession() as session:
        tasks = [
            fetch_pokemon(session, index)
            for index in range(offset + 1, offset + limit + 1)
        ]
        return await asyncio.gather(*tasks)
