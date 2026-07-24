from fastapi.testclient import TestClient
from services.ai.app.main import app

client = TestClient(app)

def test_health():
    assert client.get('/health').json()['status'] == 'ok'

def test_chunking():
    r = client.post('/chunk', json={'text': 'First paragraph.\n\nSecond paragraph.'})
    assert r.status_code == 200
    assert len(r.json()['chunks']) >= 1

def test_affinity():
    r = client.post('/affinity', json={
        'text': 'peer counselling and student wellbeing',
        'headings': [{'id': '3.2', 'title': 'Student Wellbeing', 'description': 'counselling peer support'}]
    })
    assert r.status_code == 200
    assert r.json()['mappings'][0]['score'] > 0.5
