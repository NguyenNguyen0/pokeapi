from app import app
from flask import jsonify, render_template
from app.api import get_pokemons_by_page

@app.route("/")
def index():
    DEFAULT_PAGE = 1
    result = get_pokemons_by_page(DEFAULT_PAGE)
    return render_template(
        "index.html",
        pokemons=result["pokemons"],
        next=result["next"],
        previous=result["previous"],
        page=result["page"]
    )


@app.route("/api/pokemons/<int:page>")
def api_get_pokemons_by_page(page):
    pokemons = get_pokemons_by_page(page)
    return jsonify(pokemons)


if __name__ == "__main__":
    app.run(debug=True)
