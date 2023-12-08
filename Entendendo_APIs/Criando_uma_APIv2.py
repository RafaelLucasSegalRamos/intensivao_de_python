from flask import Flask, jsonify, request
import json
import pandas as pd

app = Flask(__name__)

livro = [
    {"id": 1, "titulo": "O Senhor dos Anéis", "autor": "J.R.R. Tolkien"},
    {"id": 2, "titulo": "O Hobbit", "autor": "J.R.R. Tolkien"},
    {"id": 3, "titulo": "O Silmarillion", "autor": "J.R.R. Tolkien"},
    {"id": 4, "titulo": "O Código da Vinci", "autor": "Dan Brown"},
    {"id": 5, "titulo": "Anjos e Demônios", "autor": "Dan Brown"},
    {"id": 6, "titulo": "Fortaleza Digital", "autor": "Dan Brown"},
]


@app.route("/")
def homepage():
    return "<h1 style='font-family: Arial;''>Está é a HomePage da API<h1>"


# Mostrando todos os livros
@app.route("/livros", methods=["GET"])
def obter_livro(): 
    return jsonify(livro)


# Consultando um livro pelo seu id
@app.route("/livros/muda/<int:id>", methods=[
    "GET"])  # <int:id> é um parametro, no caso ele pega um valor inteiro na URL e coloca numa variavel chamada id
def obter_por_id(id):
    for i in livro:
        if i["id"] == id:
            return jsonify(i)
    return None


# Editando um livro pelo seu id
@app.route("/livros/<int:id>", methods=["PUT"])
def editar_por_id(id):
    livro_alt = request.get_json()
    for i, l in enumerate(livro):
        if l["id"] == id:
            livro[i].update(livro_alt)
            return jsonify(livro[i])


app.run(port=5000, host="localhost", debug=True)
