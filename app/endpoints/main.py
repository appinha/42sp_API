from flask_restplus import Resource
from app.api import api

ns_default = api.default_namespace

@ns_default.route('/hello')
class HelloWorld(Resource):
	def get(self):
		return "Hello, World!"
