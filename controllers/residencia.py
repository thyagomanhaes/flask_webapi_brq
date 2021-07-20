from flask import request
from flask_restplus import Resource, fields

from models.residencia import ResidenciaModel
from schemas.residencia import ResidenciaSchema

from server.instance import server

book_ns = server.book_ns

ITEM_NOT_FOUND = "Residencia not found."

book_schema = ResidenciaSchema()
book_list_schema = ResidenciaSchema(many=True)

# Model required by flask_restplus for expect
item = book_ns.model('Book', {
    'title': fields.String('Book title'),
    'pages': fields.Integer(0),
})

class Residencia(Resource):

    def get(self, id):
        param = request.args.get('neighbourhood_group')
        if param:
            print("PARAMETRO: ", param)
        book_data = ResidenciaModel.find_by_id(id)
        if book_data:
            return book_schema.dump(book_data)

class ResidenciaList(Resource):
    @book_ns.doc('Get all Items')
    def get(self):
        if request.args:
            args = request.args
            return book_list_schema.dump(ResidenciaModel.find_by_field(args)), 200
        else:
            return book_list_schema.dump(ResidenciaModel.find_all()), 200
    
    @book_ns.expect(item)
    @book_ns.doc('Create an Item')
    def post(self):
        residencia_json = request.get_json()
        residencia_data = book_schema.load(residencia_json)

        residencia_data.save_to_db()

        return book_schema.dump(residencia_data), 201