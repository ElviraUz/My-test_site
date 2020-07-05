from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Arenas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    adress = db.Column(db.String, nullable=False)
    website = db.Column(db.String, nullable=False)
    phones = db.Column(db.String, nullable=False)
    hours24 = db.Column(db.Boolean, nullable=False)
    description = db.Column(db.Text, nullable=False)
    image = db.Column(db.Text, nullable=False)
    metro = db.Column(db.String, nullable=False)
    everyday = db.Column(db.Boolean, nullable=False)
    brief_id = db.Column(db.Integer, db.ForeignKey('brief.id'),nullable=True)
    def __repr__(self):
        return '<Arenas {}'.format(self.name)

class Brief(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # arenas_id = db.Column(db.Integer, db.ForeignKey('arenas.id'),nullable=False)
    brief1 = db.Column(db.String, nullable=True)
    brief2 = db.Column(db.String, nullable=True)
    brief3 = db.Column(db.String, nullable=True)
    brief = db.relationship('Arenas', backref='brief', lazy=True)




# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(30), index=True, unique=True)
#     password = db.Column(db.String(20))
#     role = db.Column(db.String(10), index=True)

#     def __repr__(self):
#         return '<User {}>'.format(self.username)
