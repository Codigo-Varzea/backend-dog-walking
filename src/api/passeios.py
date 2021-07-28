from . import api
from flask import Blueprint, request, jsonify
from datetime import datetime
from src.models import Walks, Walk, WalkStatus, Pet, WalkSchema

walks = Walks()

@api.route('/passeios', methods=['GET'])
def fetch_passeios():
    schema = WalkSchema(many=True)

    total_per_page = int(request.args.get('total-per-page', 10))
    page = int(request.args.get('page', 0))

    paginated_walks = walks.fetch_by_page_index(total_per_page, page)

    return jsonify(schema.dump(paginated_walks))

@api.route('/passeios/<string:id>', methods=['GET'])
def get_passeio(id):
    walk_found = walks.get_by_id(id)

    if walk_found is None:
        return jsonify({ 'error': 'not found' }), 404

    schema = WalkSchema()
    return jsonify(schema.dump(walk_found))

@api.route('/passeios', methods=['POST'])
def post_passeio():
    walk = Walk.from_json(request.json)

    walks.create(walk)

    schema = WalkSchema()
    return jsonify(schema.dump(walk)), 201

@api.route('/passeios/<string:id>', methods=['DELETE'])
def delete_passeio(id):
    walk_found = walks.get_by_id(id)

    if walk_found is None:
        return jsonify({ 'error': 'not found' }), 404
    
    walks.delete(walk_found)

    return {}, 204

@api.route('/passeios/hoje', methods=['GET'])
def get_today_passeios():
    schema = WalkSchema(many=True)
    return jsonify(schema.dump(walks.fetch_from_start_date(datetime.today())))

@api.route('/passeios/<string:id>/duracao', methods=['GET'])
def duracao_passeio(id):
    walk_found = walks.get_by_id(id)

    if walk_found is None:
        return jsonify({ 'error': 'not found' }), 404

    return jsonify({ 'duracao': f'{walk_found.duration}' })

def change_status_or_404(id, status):
    walk_found = walks.get_by_id(id)

    if walk_found is None:
        return jsonify({ 'error': 'not found' }), 404
    
    walk_found.status = status

    walks.update(walk_found)

    schema = WalkSchema()
    return jsonify(schema.dump(walk_found))

@api.route('/passeios/<string:id>/inicio', methods=['POST'])
def inicio_passeio(id):
    return change_status_or_404(id, WalkStatus.WALKING)

@api.route('/passeios/<string:id>/fim', methods=['POST'])
def fim_passeio(id):
    return change_status_or_404(id, WalkStatus.DONE)

