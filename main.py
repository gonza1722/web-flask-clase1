import random
from flask import Flask

app = Flask(__name__)

facts_list = [
    "La mayoría de los pensamientos sobre tecnología ocurren navegando por la red.",
    "El primer servidor web de la historia fue una computadora NeXT usada por Tim Berners-Lee.",
    "Python fue creado por Guido van Rossum a finales de los años 80."
]

@app.route("/")
def home():
    return '<h1>Home page</h1><a href="/random_fact">¡Ver un dato aleatorio!</a>'

@app.route("/random_fact")
def random_fact():
    return f'<p>{random.choice(facts_list)}</p><a href="/">Volver al inicio</a>'

if __name__ == "__main__":
    app.run(debug=True)