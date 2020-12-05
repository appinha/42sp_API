from flask import Flask
from flask import Blueprint
import traceback
from app.api import api
from app.endpoints.main import ns_default

def create_app(test_config=None):
	'''
	This function creates and configures the application.
	'''
	app = Flask(__name__)

	if test_config is None:
		app.config.from_pyfile("config.py", silent=True)
	else:
		app.config.update(test_config)

	app.config['RESTPLUS_VALIDATE'] = True
	app.config['ERROR_404_HELP'] = False

	blueprint = Blueprint('api', __name__)
	api.init_app(blueprint)
	app.register_blueprint(blueprint)

	api.add_namespace(ns_default)

	return app
