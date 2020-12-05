import pytest
from app import create_app

@pytest.fixture
def app():
	'''
		This function creates and configures a new app instance for each test.
	'''
	app = create_app({"TESTING": True})
	return app

@pytest.fixture
def client(app):
	return app.test_client()
