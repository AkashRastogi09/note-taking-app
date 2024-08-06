from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from models import db, Note

app = Flask(__name__)
app.config.from_object('config.Config')
db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/api/notes', methods=['POST'])
def add_note():
    data = request.json
    new_note = Note(
        title=data.get('title'),
        content=data.get('content')
    )
    db.session.add(new_note)
    db.session.commit()
    return jsonify(new_note.serialize()), 201

@app.route('/api/notes', methods=['GET'])
def get_notes():
    notes = Note.query.all()
    return jsonify([note.serialize() for note in notes]), 200

@app.route('/api/notes/<int:id>', methods=['PUT'])
def update_note(id):
    note = Note.query.get(id)
    if note is None:
        return jsonify({'error': 'Note not found'}), 404
    data = request.json
    note.title = data.get('title')
    note.content = data.get('content')
    db.session.commit()
    return jsonify(note.serialize()), 200

@app.route('/api/notes/<int:id>', methods=['DELETE'])
def delete_note(id):
    note = Note.query.get(id)
    if note is None:
        return jsonify({'error': 'Note not found'}), 404
    db.session.delete(note)
    db.session.commit()
    return '', 204

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    