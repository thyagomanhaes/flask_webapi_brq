from ma import ma
from models.residencia import ResidenciaModel

class ResidenciaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ResidenciaModel
        load_instance = True