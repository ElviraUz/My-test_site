from flask import Flask, render_template
#from .forms import LoginForm
from webapp.model import db


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    @app.route("/")  #декоратор позволяет открывать наш сайт слэш - это локаль
    def hello():
        page_title="Киберспорт Арены"
        return render_template('index.html', page_title=page_title)

    # @app.route('/login')
    # def login():
    #     title = "Авторизация"
    #     login_form = LoginForm()
    #     return render_template("login.html",page_title=title, form=login_form)
    
    @app.route('/arena')
    def arena():
        page_title = name()
        descripton = descripton()
        metro = metro()
        website = website()
        return render_template('testarena.html', page_title=page_title)
#дописать функция для арены



    return app
# if __name__ == 'main':
#     app = create_app()
#     app.run()