from  flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Arenas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column (db.Srting, nullable = False) #Название
    adress = db.Column (db.Srting, nullable = False) #адрес
    metro = db.Column (db.Srting, nullable = False) #Название
    description = db.Column (db.Text, nullable = True) #описание
    website = db.Column(db.Srting, nullable=False)
    
    def __repr__(self):
        return '<Arenas {}'.format(self.name)