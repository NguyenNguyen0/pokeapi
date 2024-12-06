document.addEventListener('DOMContentLoaded', () => {
    const pokemonsContainer = document.querySelector('.pokemon-grid-container');
    const pokemonItems = document.querySelectorAll('.pokemon-item');

    const pokemonId = document.querySelector('.pokemon-details-id span');
    const pokemonImage = document.querySelector('.pokemon-details-img');
    const pokemonName = document.querySelector('.pokemon-details-name');
    const pokemonTypes = document.querySelector('.pokemon-details-type-container');
    const pokemonHp = document.querySelector('.pokemon-details-hp');
    const pokemonAttack = document.querySelector('.pokemon-details-attack');
    const pokemonDefense = document.querySelector('.pokemon-details-defense');
    const pokemonSpAttack = document.querySelector('.pokemon-details-sp-attack');
    const pokemonSpDefense = document.querySelector('.pokemon-details-sp-defense');
    const pokemonSpeed = document.querySelector('.pokemon-details-speed');

    const getPokemon = async (url) => {
        const response = await fetch(url);
        const data = await response.json();
        return data;
    }

    const fillPokemonDetails = async (element) => {
        const pokemon = await getPokemon(`/api/pokemons/${element.dataset.name}`);

        pokemonImage.src = pokemon.image_url;
        pokemonId.textContent = `${pokemon.id}`;
        pokemonName.textContent = pokemon.name;
        pokemonTypes.innerHTML = pokemon.types.map(type =>
            `<span class="pokemon-type ${type}">${type}</span>`
        ).join('');
        pokemonHp.textContent = pokemon.hp;
        pokemonAttack.textContent = pokemon.attack;
        pokemonDefense.textContent = pokemon.defense;
        pokemonSpAttack.textContent = pokemon.special_attack;
        pokemonSpDefense.textContent = pokemon.special_defense;
        pokemonSpeed.textContent = pokemon.speed;
    };

    const pokemonsContainerObserver = new MutationObserver((mutationsList, observer) => {
        for (let mutation of mutationsList) {
            mutation.addedNodes.forEach(addedNode => {
                addedNode.addEventListener('click', () => fillPokemonDetails(addedNode));
            });
        }
    });

    pokemonsContainerObserver.observe(pokemonsContainer, { attributes: true, childList: true, subtree: true });

    pokemonItems.forEach(pokemonItem => {
        pokemonItem.addEventListener('click', () => fillPokemonDetails(pokemonItem));
    });
});