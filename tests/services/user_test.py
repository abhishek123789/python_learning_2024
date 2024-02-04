import json
import pytest
from rest_app.core.user import UserData
from rest_app.app import app

@pytest.fixture
def client():
    client = app.test_client()
    yield client


def test_post_success(client, monkeypatch):
    # Define a sample payload
    payload = {
        "username": "test_user",
        "email": "test@example.com"
    }

    # Mock the save method
    def mock_save(self):
        return None, payload

    monkeypatch.setattr(UserData, 'save', mock_save)

    # Make a POST request to the endpoint
    response = client.post('/User/', json=payload)
    # breakpoint()
    # Assert the response status code is 201 (CREATED)
    assert response.status_code == 201

    # Assert the response contains the expected data
    data = json.loads(response.data)
    assert data['username'] == payload['username']
    assert data['email'] == payload['email']