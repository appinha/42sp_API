### Fix to Werkzeug 1.0.x issue
import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property
###
from flask_restplus import Api
import traceback

api = Api(version='1.0', title='42 API', \
			description='An API to access 42 students information.')

@api.errorhandler
def default_error_handler(e):
	message = 'An unhandled exception occurred.'
	return {'message': message}, 500
