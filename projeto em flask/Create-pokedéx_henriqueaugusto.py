
from flask import Flask, render_template
import requests

app = Flask (__name__)

def pegar_151_pokemons():
    url = "https://pokeapi.co/api/v2/pokemon?limit=151"
    resposta = requests.get(url).json()
    
    lista_pokemons = []
    
    for index, item in enumerate(resposta['results'],start=1):
        lista_pokemons.append({
            "id": index,
            "nome": item['name'].capitalize(),
            "imagem": f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{index}.png"
        })
        
    return lista_pokemons
@app.route("/")
def home():
    pokemons = pegar_151_pokemons()
    return render_template("index.html", pokemons=pokemons)

if __name__ == "__main__":
    app.run(debug=True)
    