import pytest
from app import app
from dotenv import load_dotenv
import os

load_dotenv()

assert os.getenv("SUPABASE_URL"), "SUPABASE_URL is not set"
assert os.getenv("SUPABASE_KEY"), "SUPABASE_KEY is not set"

@pytest.fixture
def app():
    app.config['TESTING'] = True
    yield app

@pytest.fixture
def client(app):
    return app.test_client()
