from db import db

class ResidenciaModel(db.Model):
    __tablename__ = "residencias"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    host_id = db.Column(db.Integer())
    host_name = db.Column(db.String(80))
    neighbourhood = db.Column(db.String(200))
    latitude = db.Column(db.Float(precision=5))
    longitude = db.Column(db.Float(precision=5))
    room_type = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))
    minimum = db.Column(db.Integer())
    number_of_reviews = db.Column(db.Integer())
    last_review = db.Column(db.Date)
    reviews_per_month = db.Column(db.Float(precision=2))
    calculated_host_listings_count = db.Column(db.Integer())
    availability_365 = db.Column(db.Integer())
    neighbourhood_group = db.Column(db.String(200))
    like = db.Column(db.Boolean())


    def __init__(self, id, name, host_id, host_name, neighbourhood, latitude, longitude, room_type,
            price, minimum, number_of_reviews, last_review, reviews_per_month, calculated_host_listings_count, availability_365,neighbourhood_group, *args, **kwargs):
        self.id = id  
        self.name = name
        self.host_id = host_id
        self.host_name = host_name
        self.neighbourhood = neighbourhood
        self.latitude = latitude
        self.longitude = longitude
        self.room_type = room_type
        self.price = price
        self.minimum = minimum
        self.number_of_reviews = number_of_reviews
        self.last_review = last_review
        self.reviews_per_month = reviews_per_month
        self.calculated_host_listings_count = calculated_host_listings_count
        self.availability_365 = availability_365
        self.neighbourhood_group = neighbourhood_group

    def __repr__(self):
        """ Special method used to represent a class's objects as a string

        Returns:
            str: string with format string
        """
        return f'ResidenciaModel(name={self.name}, neighbourhood={self.neighbourhood})'

    def json(self):
        """Transform the attributes of a class to Json format

        Returns:
            dict: Json format of attribute class
        """
        return {'name': self.name, 'neighbourhood': self.neighbourhood}

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