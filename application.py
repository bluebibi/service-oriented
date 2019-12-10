import os

from flask import Flask, render_template
import logging

from views.menus import menus_blueprint
from views.auth import auth_blueprint, kakao_oauth
from reset_server.resource import TemperatureResource, TemperatureCreationResource, TemperatureByLocationResource
from reset_server.resource_check import resource_blueprint
from flask_restful import Api

from database import base
from database.base import User
from flask_login import current_user, LoginManager

application = Flask(__name__)
application.register_blueprint(menus_blueprint, url_prefix='/menus')
application.register_blueprint(auth_blueprint, url_prefix='/auth')
application.register_blueprint(resource_blueprint, url_prefix='/resource')

application.config['WTF_CSRF_SECRET_KEY'] = os.urandom(24)
application.config['SECRET_KEY'] = os.urandom(24)

login_manager = LoginManager()
login_manager.init_app(application)

@login_manager.user_loader
def load_user(user_id):
    q = base.db_session.query(User).filter(User.id == user_id)
    user = q.first()

    if user is not None:
        user._authenticated = True
    return user


api = Api(application)
api.add_resource(TemperatureResource, "/resource/<sensor_id>")
api.add_resource(TemperatureCreationResource, "/resource_creation")
api.add_resource(TemperatureByLocationResource, "/resource_location/<location>")

logging.basicConfig(
    filename='test.log',
    level=logging.DEBUG
)

# @app.route("/")
# def hello_work():
#     logging.error("root!!!!")
#     return "<h1>Hello World!!!!!!!!!!!!!!!!!!!!!</h1>"

@application.route('/')
def hello_html():
    return render_template(
        'index.html',
        nav_menu="home",
        current_user=current_user,
        kakao_oauth=kakao_oauth
    )

if __name__ == "__main__":
    logging.info("Flask Web Server Started!!!")

    application.debug = True
    application.config['DEBUG'] = True

    application.run(host="localhost", port="8080")
