import pytest
from app import app as flask_app
from dotenv import load_dotenv
import os

load_dotenv()

assert os.getenv("SUPABASE_URL"), "SUPABASE_URL is not set"
assert os.getenv("SUPABASE_KEY"), "SUPABASE_KEY is not set"

@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""
    flask_app.config['TESTING'] = True
    flask_app.config['DEBUG'] = False
    return flask_app

@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()

@pytest.fixture
def runner(app):
    """A test runner for the app's Click commands."""
    return app.test_cli_runner()
