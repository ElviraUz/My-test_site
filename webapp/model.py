from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Arenas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=True)
    adress = db.Column(db.String, nullable=True)
    metro = db.Column(db.String, nullable=True)
    description = db.Column(db.Text, nullable=True)
    website = db.Column(db.String, nullable=True)
    phone = db.Column(db.String, nullable=True)
    image = db.Column(db.String, nullable=True)
    hours24 = db.Column(db.Boolean, nullable=True) 
    def __repr__(self):
        return '<Arenas {}'.format(self.name)

