from itertools import count
from flask import Flask, request, jsonify
from flask_pydantic_spec import (
    FlaskPydanticSpec, Response, Request
)
from pydantic import BaseModel, Field
from tinydb import TinyDB, Query
from typing import Optional
from tinydb.storages import MemoryStorage

app = Flask(__name__)
spec = FlaskPydanticSpec('YutaFlask', title='Yuta Api Rest')
spec.register(app)
database = TinyDB(storage=MemoryStorage)
c = count()

# Codigo de respostas https://http.cat/
    
class QueryPessoa(BaseModel):
    id: Optional[int]
    nome: Optional[str]
    idade: Optional[int]
    
class Pessoa(BaseModel):
    id: Optional[int] = Field(default_factory=lambda: next(c))
    nome: str
    idade: int

class Pessoas(BaseModel):
    pessoas: list[Pessoa]
    count: int

@app.get('/pessoas') # Rota, endpoint, recurso ...
@spec.validate(query=QueryPessoa,resp=Response(HTTP_200=Pessoas))
def buscar_pessoas():
    """ Retorna todas as pessoas do banco de dados """
    query = request.context.query.dict(exclude_none=True)
    todas_as_pessoas = database.search(
        Query().fragment(query)
    )
    return jsonify(
        Pessoas(
            pessoas=todas_as_pessoas,
            count=len(todas_as_pessoas)
        ).dict()
    )
    
@app.get('/pessoas/<int:id>') # Rota, endpoint, recurso ...
@spec.validate(resp=Response(HTTP_200=Pessoa))
def buscar_pessoa(id):
    """ Retorna uma pessoa por id do banco de dados """
    try:
        pessoa = database.search(Query().id == id)[0]
    except IndexError: 
        return {'message': 'Pessoa not found!'}, 404
    return jsonify(pessoa)

@app.post('/pessoas')
@spec.validate(body=Request(Pessoa), resp=Response(HTTP_200=Pessoa))
def inserir_pessoas():
    """ Insere uma Pessoa no banco de dados """
    body = request.context.body.dict()
    database.insert(body)
    return body

@app.put('/pessoas/<int:id>')
@spec.validate(body=Request(Pessoa), resp=Response(HTTP_201=Pessoa))
def mudar_pessoas(id):
    """Muda nome, id e idade da pessoa do banco de dados"""
    pessoa = Query()
    body = request.context.body.dict()
    database.update(body, pessoa.id == id)
    return jsonify(body)


@app.delete('/pessoas/<int:id>')
@spec.validate(resp=Response('HTTP_204'))
def deletar_pesssoa(id):
    """Remove uma pessoa do banco de dados por id"""
    pessoa = Query()
    database.remove(pessoa.id == id)
    return jsonify({})
    
verdoc = input(str("Dijite 'D' para ver a doc = "))

if verdoc == 'D':
    # Adicione mais rotas conforme necessário

    # Função para listar rotas
    def listar_rotas():
        output = []
        for rule in app.url_map.iter_rules():
            methods = ','.join(rule.methods)
            line = f"{rule.endpoint} {methods} {rule}"
            output.append(line)
        return '\n'.join(output)

    # Exemplo de como utilizar a função para listar rotas
    if __name__ == '__main__':
        print("Rotas disponíveis:")
        print(listar_rotas())
else:
    app.run()