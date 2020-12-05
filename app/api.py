### Fix to Werkzeug 1.0.x issue
import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property
###
from flask_restplus import Api


api = Api(version='1.0', title='42 API', \
			description='An API to access 42 students information.')
