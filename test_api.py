from fastapi.testclient import TestClient
from main import app
client = TestClient(app)

def test_positive_sentiment():
    response = client.post("/analyze", json={"text": "I love this new product, it's amazing!"})
    assert response.status_code == 200
    assert "positive" in response.json()['result'][0]['label'].lower()

def test_negative_sentiment():
    response = client.post("/analyze", json={"text": "I hate this new product, it's terrible!"})
    assert response.status_code == 200
    assert "negative" in response.json()['result'][0]['label'].lower()

def test_empty_text():
    response = client.post("/analyze", json={"text": " "})
    assert response.status_code == 400  
    assert "must not be empty" in response.json()['detail'].lower()
