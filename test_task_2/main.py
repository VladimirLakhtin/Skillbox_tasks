from http import client
import mimetypes
from flask import Flask, jsonify, request
from werkzeug.utils import secure_filename
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base


app = Flask(__name__)

client = app.test_client()

engine = create_engine('postgresql://postgres:1913131@localhost:5432')

session = scoped_session(sessionmaker(
    autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()
Base.query = session.query_property()

from model import *

Base.metadata.create_all(bind=engine)

@app.route('/kitties', methods=['GET'])
def get_list():
    kitties = Kitties.query.all()
    serialised = []

    for kitty in kitties:
        serialised.append({
            'id': kitty.id,
            'name': kitty.name,
            'age': kitty.age,
            'breed': kitty.breed,
            'description': kitty.description,
            'image_url': kitty.image_url
        })

    return jsonify(serialised)

@app.route('/kitties', methods=['POST'])
def update_list():
    print(request.json)
    new_one = Kitties(**request.json)

    session.add(new_one)
    session.commit()
    
    serialized = {
        'id': new_one.id,
        'name': new_one.name,
        'age': new_one.age,
        'breed': new_one.breed,
        'description': new_one.description,
        'image_url': new_one.image_url
    }

    return jsonify(serialized)

@app.route('/kitties/<int:kitty_id>', methods=['PUT'])
def update_kitty(kitty_id):
    item = Kitties.query.filter(Kitties.id == kitty_id).first()
    params = request.json

    if not item:
        return {'message': 'No kitties with this id'}, 400

    for key, value in params.items():
        setattr(item, key, value)

    session.commit()
    serialized = {
        'id': item.id,
        'name': item.name,
        'age': item.age,
        'breed': item.breed,
        'description': item.description,
        'image_url': item.image_url
    }

    return serialized

@app.route('/kitties/<int:kitty_id>', methods=['DELETE'])
def delete_kitty(kitty_id):
    item = Kitties.query.filter(Kitties.id == kitty_id).first()
    if not item:
        return {'message': 'No kitties with this id'}, 400
    session.delete(item)
    session.commit()
    return '', 204


@app.teardown_appcontext
def shutdown_session(exception=None):
    session.remove()

if __name__ == "__main__":
    app.run()







