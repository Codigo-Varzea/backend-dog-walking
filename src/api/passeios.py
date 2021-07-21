from . import api
from flask import Blueprint, request, jsonify
from src.models import Walks, Walk, WalkStatus, Pet

walks = Walks()
## Rotas da API
# - api/v0.1/passeios (GET)
# - api/v0.1/passeios?pagina=0 (GET)
# - api/v0.1/passeios (POST)
# - api/v0.1/passeios (PUT)
# - api/v0.1/passeios (DELETE)
# - api/v0.1/passeios/hoje (GET)
# - api/v0.1/passeios/duracao (GET)
# - api/v0.1/passeios/inicio (GET)
# - api/v0.1/passeios/fim (GET)

@api.route('/passeios', methods=['GET'])
def fetch_passeios():
    return jsonify(passeios=walks.fetch_all())

@api.route('/passeios/<int:id>', methods=['GET'])
def get_passeio():
    return jsonify(passeios=walks.fetch_all())

@api.route('/passeios', methods=['POST'])
def post_passeio():
    walk = Walk.from_json(request.json)
    walks.create(walk)
    return jsonify(walk)