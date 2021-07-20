from db import db

class PrecoMedioModel(db.Model):
    __tablename__ = "preco_medio"

    id = db.Column(db.Integer, primary_key=True)
    neighbourhood_group = db.Column(db.String(200), nullable=False)
    room_type = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Float(precision=5), nullable=False)

    def __init__(self, id, neighbourhood_group, room_type, price, *args, **kwargs):
        self.id = id
        self.neighbourhood_group = neighbourhood_group  
        self.room_type = room_type
        self.price = price


    def __repr__(self):
        """ Special method used to represent a class's objects as a string

        Returns:
            str: string with format string
        """
        return f'ResidenciaModel(name={self.neighbourhood_group}, neighbourhood={self.room_type})'

    def json(self):
        """Transform the attributes of a class to Json format

        Returns:
            dict: Json format of attribute class
        """
        return {'name': self.neighbourhood_group, 'neighbourhood': self.room_type}

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_all(cls):
        return cls.query.all()

    @classmethod
    def find_by_field(cls, args):
        return cls.query.filter_by(**args).all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()