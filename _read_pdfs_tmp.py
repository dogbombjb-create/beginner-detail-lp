import os, sys
from pypdf import PdfReader
folder='"'"'docs'"'"'
for name in os.listdir(folder):
    path=os.path.join(folder,name)
    if os.path.getsize(path)>1_000_000:
        continue
    try:
        reader=PdfReader(path)
        text='"'"''.join((p.extract_text() or '"'"'') for p in reader.pages[:3])
        out = ('"'"'\n--- '"'"'+name+'"'"'\n'"'"'+ (text[:1200] or '"'"'').replace('"'"'\n'"'"','"'"' '"'"')).encode('"'"'utf-8'"'"','"'"'ignore'"'"')
        sys.stdout.buffer.write(out+b'"'"'\n'"'"')
    except Exception as e:
        sys.stdout.buffer.write(f"\n--- {name} ERROR {e}\n".encode('"'"'utf-8'"'"','"'"'ignore'"'"'))
