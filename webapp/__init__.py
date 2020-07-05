from flask import Flask, render_template
from .model import db, Arenas, Brief
from flask import abort


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    @app.route("/")  #декоратор позволяет открывать наш сайт, слэш - это локаль
    def hello():
        page_title = "Киберспорт Арены"
        return render_template('index.html', page_title=page_title)


    @app.route('/main')
    def main_page():
        page_title="Киберспорт в Москве"
        return render_template ('main.htm', page_title=page_title)

	# @app.route('/catalogue')
	# def catalogue_page
	# 	page_title= "Каталог киберспорт арен"
	#     return render_template ('main.htm', page_title=page_title)

    @app.route('/arena/<int:arenas_id>')
    def arena(arenas_id):
        arena= Arenas.query.get(arenas_id)
        brief=Brief.query.get(arena.brief_id)
	#   if not arenas_id:
	#   	abort (404)

        return render_template('testarena.html', page_title=arena.name, arena=arena, brief=brief )

    return app