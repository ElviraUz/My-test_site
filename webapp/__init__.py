from flask import Flask, render_template
from .model import db, Arenas, Brief
#from flask import abort
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    admin = Admin(app)

    admin.add_view(ModelView(Arenas, db.session))
    admin.add_view(ModelView(Brief, db.session))

    @app.route("/")
    def hello():
        page_title = "Киберспорт Арены"
        return render_template('index.html', page_title=page_title)


    @app.route('/main')
    def main_page():
        page_title = "Киберспорт в Москве"
        return render_template ('main.htm', page_title=page_title)

    @app.route('/catalogue')
    def catalogue_page():
        page_title = "Все киберспорт арены Москвы"
        arena = Arenas.query.get (arenas_id)
        
        return render_template ('catalogue.html', page_title=page_title, arena=arena,)


    @app.route('/arena/<int:arenas_id>')
    def arena(arenas_id):
        arena = Arenas.query.get(arenas_id)
        brief = Brief.query.get(arena_brief_id)

	#   if not arenas_id:
	#   	abort (404)
        return render_template('testarena.html', arena=arena, brief=brief)

    return app

