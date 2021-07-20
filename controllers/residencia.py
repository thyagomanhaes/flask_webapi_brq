from flask import request
from flask_restplus import Resource, fields

from models.residencia import ResidenciaModel
from schemas.residencia import ResidenciaSchema

from server.instance import server
from db import db

residencia_ns = server.residencia_ns

ITEM_NOT_FOUND = "Residencia not found."

residencia_schema = ResidenciaSchema()
residencia_list_schema = ResidenciaSchema(many=True)

# Model required by flask_restplus for expect
item = residencia_ns.model('Residencia', {
    'id': fields.Integer(description='id da propriedade'),
    'like': fields.Boolean(),
})

class Residencia(Resource):

    def get(self, id):
        residencia_data = ResidenciaModel.find_by_id(id)
        if residencia_data:
            return residencia_schema.dump(residencia_data)
        return {'message': ITEM_NOT_FOUND},404

class ResidenciaList(Resource):
    @residencia_ns.doc('Get all Items')
    def get(self):
        if request.args:
            args = request.args
            return residencia_list_schema.dump(ResidenciaModel.find_by_field(args)), 200
        else:
            return residencia_list_schema.dump(ResidenciaModel.find_all()), 200
    
    @residencia_ns.expect(item)
    @residencia_ns.doc('Create an Item')
    def post(self):
        residencia_json = request.get_json()
        residencia_data = residencia_schema.load(residencia_json, session=db.session) # Transforma o dicionário em um objeto que pode ser utilizado pelo banco de dados
        residencia_data.save_to_db()

        return residencia_schema.dump(residencia_data), 201