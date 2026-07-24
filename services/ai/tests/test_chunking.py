from fastapi.testclient import TestClient
from services.ai.app.main import app
client=TestClient(app)

def test_hierarchy_aware_chunking_preserves_paths():
    blocks=[
      {'id':'h1','type':'heading','level':1,'text':'3 Student Support','order':1,'page':1},
      {'id':'h2','type':'heading','level':2,'text':'3.1 Counselling Services','order':2,'page':1},
      {'id':'p1','type':'paragraph','text':'The unit conducted 18 counselling sessions for 460 students in August 2025.','order':3,'page':1}
    ]
    r=client.post('/chunk',json={'blocks':blocks,'target_tokens':100,'document_context':{'unit':'Student Affairs'}})
    assert r.status_code==200
    c=r.json()['chunks'][0]
    assert c['headingPath']==['3 Student Support','3.1 Counselling Services']
    assert c['type'] in ('event','metric')
    assert c['blockIds']==['h2','p1']

def test_tables_are_atomic_chunks():
    blocks=[{'id':'h','type':'heading','level':1,'text':'Research Outputs','order':1,'page':1},{'id':'t','type':'table','caption':'Publications','columns':['Type','Count'],'rows':[['Journal','42']], 'order':2,'page':1}]
    r=client.post('/chunk',json={'blocks':blocks,'target_tokens':5,'preserve_tables':True})
    assert r.status_code==200
    assert any(c['type']=='table' and 'Journal' in c['text'] for c in r.json()['chunks'])
