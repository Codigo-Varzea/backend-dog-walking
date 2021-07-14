from flask import Blueprint, jsonify
from src.models import Walks, Walk, WalkStatus, Pet

passeios = Blueprint('passeios', __name__, url_prefix='/passeios')

walks = Walks()

@passeios.route('/', methods=['GET'])
def fetch_passeios():
    return jsonify(passeios=walks.fetch_all())

@passeios.route('/<int:id>', methods=['GET'])
def get_passeio():
    return jsonify(passeios=walks.fetch_all())