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

    app.config["SECRET_KEY"] = "mysecret"

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
        arenas = Arenas.query.all()[:9]
        print(arenas)
        page_title = "Все киберспорт арены "     
        return render_template('catalogue.html', page_title=page_title,arenas=arenas)


    @app.route('/arena/<int:arenas_id>')
    def arena(arenas_id):
        arena = Arenas.query.get(arenas_id)
        brief = Brief.query.get(arena.brief_id)

	#   if not arenas_id:
	#   	abort (404)
        return render_template('testarena.html', arena=arena, brief=brief)

    return app
