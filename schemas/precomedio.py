from ma import ma
from models.precomedio import PrecoMedioModel

class PrecoMedioSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = PrecoMedioModel
        load_instance = True