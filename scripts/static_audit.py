from pathlib import Path
import json,re,sys
root=Path(__file__).resolve().parents[1]
errors=[]
for f in (root/'data').glob('*.json'):
    try: json.loads(f.read_text())
    except Exception as e: errors.append(f"invalid JSON {f.name}: {e}")
required=['apps/web/src/App.tsx','apps/api/src/index.ts','services/ai/app/main.py']
for x in required:
    if not (root/x).exists(): errors.append(f"missing {x}")
text='\n'.join(f.read_text(errors='ignore') for f in root.rglob('*') if f.is_file() and 'node_modules' not in f.parts)
for label,pat in [('demo parsing control',r'Complete demo job'),('empty upload payload',r"contentBase64:\s*['\"]{2}")]:
    if re.search(pat,text): print('WARNING:',label)
print('Static audit:', 'PASS' if not errors else 'FAIL')
for e in errors: print('ERROR:',e)
sys.exit(bool(errors))
