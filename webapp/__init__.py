from flask import Flask, render_template
from .model import db, Arenas


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    @app.route("/")  #декоратор позволяет открывать наш сайт, слэш - это локаль
    def hello():
        page_title = "Киберспорт Арены"
        return render_template('index.html', page_title=page_title)

    @app.route('/arena')
    def arena():
        arena = Arenas.query.filter(Arenas.id == 1).first()
        #такая функция должна быть у каждой страницы для рендера
        return render_template('testarena.html', arena=arena)

    return app
