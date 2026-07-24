import base64, io
from fastapi.testclient import TestClient
from openpyxl import Workbook
from services.ai.app.main import app
client=TestClient(app)

def test_xlsx_structure_import_preserves_sheet_and_table():
    wb=Workbook();ws=wb.active;ws.title='Academic Development';ws.append(['Metric','Value']);ws.append(['Students',2000]);buf=io.BytesIO();wb.save(buf)
    r=client.post('/parse',json={'file_name':'structure.xlsx','content_base64':base64.b64encode(buf.getvalue()).decode()})
    assert r.status_code==200
    blocks=r.json()['blocks']
    assert blocks[0]['type']=='heading'
    assert any(b['type']=='table' for b in blocks)

def test_five_level_numbered_text_is_detected():
    r=client.post('/parse',json={'file_name':'structure.txt','text':'1 Chapter\n1.1 Section\n1.1.1 Subsection\n1.1.1.1 Detail\n1.1.1.1.1 Final'})
    assert r.status_code==200
    levels=[b.get('level') for b in r.json()['blocks'] if b['type']=='heading']
    assert levels==[1,2,3,4,5]
