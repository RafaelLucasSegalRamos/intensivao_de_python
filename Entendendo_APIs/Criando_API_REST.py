from typing import Optional

from flask import Flask, jsonify, request
from flask_pydantic_spec import FlaskPydanticSpec, Request, Response
from pydantic import BaseModel, Field
from tinydb import Query, TinyDB

app = Flask(__name__)
spec = FlaskPydanticSpec("flask", title="Teste online")
spec.register(app)
database = TinyDB("minha_tabela.json")

class Pessoa(BaseModel):
      id: Optional[int]
      nome: str
      idade: int


class Pessoas(BaseModel):
      pessoas: list[Pessoa]
      count: int


@app.get("/")
def home():
      return """
            <h1 style='font-family: Arial;''>Está é a HomePage da API</h1>
            <p>Para ir para a pagina da API segue o link: <a href='/pessoas'>API</a></p>
              """


@app.get("/pessoas")
@spec.validate(resp=Response(HTTP_200=Pessoas))
def pessoas():
      return jsonify(
          Pessoas(pessoas=database.all(), count=len(database.all())).dict())
      return jsonify(database.all())


# Para fazer um debug o melhor jeito é utilizando o Swagger, meu link por exemplo é https://python-api.rafaelramos811.repl.co/apidoc/swagger#/


@app.post("/pessoas")
@spec.validate(body=Request(Pessoa), resp=Response(HTTP_200=Pessoa))
def inserir_pessoas():
      body = request.context.body.dict()
      body["nome"] = body["nome"].capitalize()
      database.insert(body)
      return jsonify(body)


@app.put("/pessoas/<int:id>")
@spec.validate(body=Request(Pessoa), resp=Response(HTTP_200=Pessoa))
def altera_pessoas(id: int):
      body = request.context.body.dict()
      database.update(
          body, Query().id == id
      )  # Update(nova_informação, onde_mudar) no caso a nova_informação é a variavel body e o onde_mudar é onde o ID é igual a variavel id escolhida.
      return jsonify(body)

@app.get("/pessoas/<int:id>")
@spec.validate(resp=Response(HTTP_200=Pessoas))
def procura_id_pessoas(id: int):
      pessoa = database.search(Query().id == id)
      return jsonify(pessoa)


@app.delete("/pessoas/<int:id>")
@spec.validate(resp=Response("HTTP_204"))
def remove_pessoas(id: int):
      database.remove(
          Query().id == id
      )  # remove(onde_mudar) O onde_mudar é onde o ID é igual a variavel id escolhida, e diferente do update o delete só precisa de uma entrada.
      return "Arquivo deletado"


app.run(host="0.0.0.0", port=8080)
