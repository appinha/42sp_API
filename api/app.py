from flask import Flask, Blueprint
from api.restplus import api
from api.endpoints.main import ns_default

app = Flask(__name__)

def initialize_app(app):
	app.config['RESTPLUS_VALIDATE'] = True
	app.config['ERROR_404_HELP'] = False

	blueprint = Blueprint('api', __name__)
	api.init_app(blueprint)
	app.register_blueprint(blueprint)

	api.add_namespace(ns_default)

def main():
	initialize_app(app)
	app.run(debug=True)


if __name__ == '__main__':
	main()
