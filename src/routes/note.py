from flask import Blueprint, jsonify, request
from src.models.note_mongo import Note, notes_collection
from datetime import datetime

note_bp = Blueprint('note', __name__)

@note_bp.route('/notes', methods=['GET'])
def get_notes():
    """Get all notes, ordered by most recently updated"""
    notes = notes_collection.find().sort('updated_at', -1)
    return jsonify([Note.from_dict(note).to_dict() for note in notes])

@note_bp.route('/notes', methods=['POST'])
def create_note():
    """Create a new note"""
    data = request.json
    if not data or 'title' not in data or 'content' not in data:
        return jsonify({'error': 'Title and content are required'}), 400
    note = Note(title=data['title'], content=data['content'])
    result = notes_collection.insert_one({
        'title': note.title,
        'content': note.content,
        'created_at': note.created_at,
        'updated_at': note.updated_at
    })
    note.id = str(result.inserted_id)
    return jsonify(note.to_dict()), 201

@note_bp.route('/notes/<note_id>', methods=['GET'])
def get_note(note_id):
    """Get a specific note by ID"""
    from bson import ObjectId
    note = notes_collection.find_one({'_id': ObjectId(note_id)})
    if not note:
        return jsonify({'error': 'Note not found'}), 404
    return jsonify(Note.from_dict(note).to_dict())

@note_bp.route('/notes/<note_id>', methods=['PUT'])
def update_note(note_id):
    """Update a specific note"""
    from bson import ObjectId
    data = request.json
    if not data:
        return jsonify({'error': 'No data provided'}), 400
    note = notes_collection.find_one({'_id': ObjectId(note_id)})
    if not note:
        return jsonify({'error': 'Note not found'}), 404
    updated = {
        'title': data.get('title', note['title']),
        'content': data.get('content', note['content']),
        'created_at': note['created_at'],
        'updated_at': datetime.utcnow()
    }
    notes_collection.update_one({'_id': ObjectId(note_id)}, {'$set': updated})
    updated_note = notes_collection.find_one({'_id': ObjectId(note_id)})
    return jsonify(Note.from_dict(updated_note).to_dict())

@note_bp.route('/notes/<note_id>', methods=['DELETE'])
def delete_note(note_id):
    """Delete a specific note"""
    from bson import ObjectId
    result = notes_collection.delete_one({'_id': ObjectId(note_id)})
    if result.deleted_count == 0:
        return jsonify({'error': 'Note not found'}), 404
    return '', 204

@note_bp.route('/notes/search', methods=['GET'])
def search_notes():
    """Search notes by title or content"""
    query = request.args.get('q', '')
    if not query:
        return jsonify([])
    notes = notes_collection.find({
        '$or': [
            {'title': {'$regex': query, '$options': 'i'}},
            {'content': {'$regex': query, '$options': 'i'}}
        ]
    }).sort('updated_at', -1)
    return jsonify([Note.from_dict(note).to_dict() for note in notes])

