from fastapi.testclient import TestClient
from services.ai.app.main import app
c=TestClient(app)
def test_parse_text_structure():
    r=c.post('/parse',json={'file_name':'report.txt','text':'1 Introduction\nThis is a report.\n2 Activities\n- Workshop conducted'})
    assert r.status_code==200
    x=r.json();assert x['blockCount']==4;assert x['blocks'][0]['type']=='heading'
def test_health_capabilities():
    x=c.get('/health').json();assert 'docx' in x['capabilities']
