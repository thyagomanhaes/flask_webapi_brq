from flask import request
from flask_restplus import Resource, fields

from models.precomedio import PrecoMedioModel
from schemas.precomedio import PrecoMedioSchema

from server.instance import server

residencia_ns = server.residencia_ns

ITEM_NOT_FOUND = "Residencia not found."

preco_medio_schema = PrecoMedioSchema()
preco_medio_list_schema = PrecoMedioSchema(many=True)


class PrecoMedio(Resource):

    def get(self, id):
        preco_medio_data = PrecoMedioModel.find_by_id(id)
        if preco_medio_data:
            return preco_medio_schema.dump(preco_medio_data)

class PrecoMedioList(Resource):
    @residencia_ns.doc('Get all Items')
    def get(self):
        if request.args:
            args = request.args
            data = preco_medio_list_schema.dump(PrecoMedioModel.find_by_field(args))
            if len(data) == 0:
                return {'message': 'No results found'}, 404
            else:
                return data, 200
        else:
            data = preco_medio_list_schema.dump(PrecoMedioModel.find_all()), 200
            print(data)
            return data, 200
    
