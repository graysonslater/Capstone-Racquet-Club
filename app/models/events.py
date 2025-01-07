# imports database instance, the schema variable, method for adding a prefix to table names
from .db import db, environment, SCHEMA, add_prefix_for_prod

class Events(db.Model):
    __tablename__ = "events"

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}
    
    id = db.Column(db.Integer, primary_key=True)
    event_name = db.Column(db.String(100), nullable=False)
    registration_price = db.Column(db.Integer, nullable=False)
    event_date = db.Column(db.Date, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'event_name': self.event_name,
            'registration_price': self.registration_price,
            'event_date': self.event_date         
        }