#!/usr/bin/env python3
"""Verify that verbatim knowledge files match SOURCE_MANIFEST.json.

  python tools/verify_manifest.py            # check; exit 1 on any drift
  python tools/verify_manifest.py --update   # re-record hashes after an approved edit
"""
import hashlib, json, sys
from pathlib import Path

root = Path(__file__).resolve().parent.parent
mf = root / 'SOURCE_MANIFEST.json'
data = json.loads(mf.read_text(encoding='utf-8'))
update = '--update' in sys.argv
bad = 0
for e in data['files']:
    p = root / e['path']
    if not p.exists():
        print('MISSING', e['path']); bad += 1; continue
    b = p.read_bytes(); h = hashlib.sha256(b).hexdigest()
    if h != e['sha256']:
        if update:
            print('UPDATED', e['path']); e['sha256'] = h; e['bytes'] = len(b); e['edited'] = True
        else:
            print('CHANGED', e['path']); bad += 1
if update:
    mf.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding='utf-8')
print(f"{'PASS' if not bad else 'FAIL'}: {len(data['files'])} files, {bad} problems")
sys.exit(1 if bad else 0)
