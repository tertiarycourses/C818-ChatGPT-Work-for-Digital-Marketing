from pathlib import Path
import re,zipfile,sys,json
R=Path(__file__).resolve().parents[1]
patterns=[('private key',r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----'),('OpenAI key',r'\bsk-(?:proj-)?[A-Za-z0-9_-]{32,}\b'),('GitHub token',r'\b(?:ghp_|github_pat_)[A-Za-z0-9_]{25,}\b'),('Slack token',r'\bxox[baprs]-[A-Za-z0-9-]{20,}\b'),('Google API key',r'\bAIza[A-Za-z0-9_-]{30,}\b'),('AWS key',r'\bAKIA[A-Z0-9]{16}\b')]
private={'reference','assessment','archive','.git','node_modules','.venv','__pycache__'};hits=[];count=0
for p in R.rglob('*'):
 if not p.is_file() or any(x in private for x in p.relative_to(R).parts) or p.name.startswith('.env'):continue
 count+=1;text=''
 if re.search(r'answer[ _-]*(?:key|to)|marking[ _-]*(?:guide|scheme)',p.name,re.I):hits.append((str(p.relative_to(R)),'private assessment filename'))
 if p.suffix in ['.pptx','.docx']:
  with zipfile.ZipFile(p) as z:text='\n'.join(z.read(n).decode(errors='ignore') for n in z.namelist() if n.endswith('.xml'))
 elif p.suffix in ['.md','.txt','.py','.json','.html','.js','.css','.sh','.csv'] or p.name=='.gitignore':text=p.read_text(errors='ignore')
 else:continue
 for label,rx in patterns:
  for m in re.finditer(rx,text):hits.append((str(p.relative_to(R))+':'+str(text.count('\n',0,m.start())+1),label))
print('Scanned',count,'public candidate files')
for where,label in hits:print(where,label)
if hits:sys.exit(1)
print('PASS: no credential or private assessment filename patterns found')
