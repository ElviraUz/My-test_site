from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
import os.path

app = Flask(__name__)


db = SQLAlchemy(app)

admin = Admin(app)

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
    brief_id = db.Column(db.Integer, db.ForeignKey('brief.id'), nullable=True)

    def __repr__(self):
        return '<Arenas %r>' % (self.name)



class Brief(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brief1 = db.Column(db.String, nullable=True)
    brief2 = db.Column(db.String, nullable=True)
    brief3 = db.Column(db.String, nullable=True)

    brief = db.relationship('Arenas', backref='brief', lazy=True)

    def __repr__(self):
        return '<Brief %r>' % (self.id)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(30), nullable=False)
    first_name = db.Column(db.String(30), nullable=True)
    last_name = db.Column(db.String(30), nullable=True)

    def __repr__(self):
        return '<Users %r>' % (self.id)


admin.add_view(ModelView(Arenas, db.session))
admin.add_view(ModelView(Brief, db.session))
admin.add_view(ModelView(Users, db.session))

if __name__=='__main__':
    app.run(debug=True)