document.addEventListener('DOMContentLoaded', () => {
    const prevButtons = Array.from(document.querySelectorAll('.previous-page'));
    const nextButtons = Array.from(document.querySelectorAll('.next-page'));
    const pageNumberLabels = Array.from(document.querySelectorAll('.page-number'));
    const pokemonsContainer = document.querySelector('.pokemon-grid-container');

    const getPokemons = async (url) => {
        const response = await fetch(url);
        const data = await response.json();
        return data;
    }

    const navigateToPage = async (url) => {
        const data = await getPokemons(url);
        renderPokemons(data);
        pageNumberLabels.forEach(pageNumberLabel => pageNumberLabel.textContent = data.page);
        nextButtons.forEach(nextButton => nextButton.dataset.url = data.next);
        prevButtons.forEach(prevButton => {
            prevButton.dataset.url = data.previous;
            if (data.previous === null) {
                prevButton.disabled = true;
            } else {
                prevButton.disabled = false;
            }
        });
    }

    const renderPokemons = async (data) => {
        const pokemons = data.pokemons.map(pokemon =>
            `<div class="pokemon-item">
                <h3 class="pokemon-id"># <span>${pokemon.id}</span></h3>

                <div class="img-container">
                    <img class="pokemon-img" src="${pokemon.image_url}" onerror="this.onerror=null;this.src='../static/img/fallback.png';" alt="${pokemon.name}">
                </div>

                <div class="pokemon-info-container">
                    <h3 class="pokemon-name">${pokemon.name}</h3>
                    <div class="pokemon-apperance-info">
                        <h4 class="pokemon-weight"><span>${pokemon.weight}</span> kg</h4>
                        <h4 class="pokemon-height"><span>${pokemon.height}</span> m</h4>
                    </div>

                    <div class="pokemon-type-container">
                        ${pokemon.types.map(type => `<span class="pokemon-type ${type}">${type}</span>`).join('')}
                    </div>
                </div>
            </div>`
        );
        pokemonsContainer.innerHTML = pokemons.join('');
    };

    prevButtons.forEach(prevButton => prevButton.addEventListener('click', async () => {
        const url = prevButton.dataset.url;
        navigateToPage(url);
    }));

    nextButtons.forEach(nextButton => nextButton.addEventListener('click', async () => {
        const url = nextButton.dataset.url;
        navigateToPage(url);
    }));
});