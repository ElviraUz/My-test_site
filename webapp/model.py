from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Arenas(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String,nullable=False) #Название
    adress = db.Column(db.String,nullable=False) #адрес
    metro = db.Column(db.String,nullable=False)  #Название
    description = db.Column(db.Text,nullable=True) #описание
    website = db.Column(db.String,nullable=False)

    def __repr__(self):
        return '<Arenas {}'.format(self.name)    

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), index=True, unique=True)
    password = db.Column(db.String(20))
    role = db.Column(db.String(10), index=True)

    def __repr__(self):
        return '<User {}>'.format(self.username)