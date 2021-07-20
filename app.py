from flask import jsonify
from marshmallow import ValidationError

from ma import ma
from db import db
from controllers.residencia import Residencia, ResidenciaList, book_ns

from server.instance import server

api = server.api
app = server.app

@app.before_first_request
def create_tables():
    db.create_all()

api.add_resource(ResidenciaList, '/residencias')
api.add_resource(Residencia, '/residencias/<int:id>')

if __name__ == '__main__':
    db.init_app(app)
    ma.init_app(app)
    server.run()
