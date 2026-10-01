"""Verify the current Drive tree and storefront links without printing secrets."""
from pathlib import Path
import subprocess,json,hashlib,re,importlib.util,os,urllib.request
R=Path(__file__).resolve().parents[1];ROOT='1qbSKE3eIMsmUYZbG-wQ7xrwPpuAroqLr'
def rc(args):
 r=subprocess.run(['rclone',*args,'--drive-root-folder-id',ROOT],capture_output=True,text=True)
 if r.returncode:raise RuntimeError(r.stderr[:600])
 return json.loads(r.stdout)
def md5(p):return hashlib.md5(p.read_bytes()).hexdigest()
def inventory():return rc(['lsjson','gdrive:','--recursive','--files-only','--hash'])
def verify_drive():
 files=inventory();current={f['Path']:f for f in files if '/archive/' not in f['Path']}
 expected={}
 for p in (R/'courseware').glob('*'):
  if p.suffix not in ['.pdf','.pptx','.docx']:continue
  folder='Learner Guide' if p.name.startswith('LG-') else ('Lesson Plan' if p.name.startswith('LP-') else ('Trainer Slides' if p.suffix=='.pptx' else 'Learner Slides'))
  expected[folder+'/'+p.name]=p
 for p in (R/'labs').rglob('*'):
  if p.is_file() and p.name!='.DS_Store':expected['Activities/'+str(p.relative_to(R/'labs'))]=p
 bad=[]
 for key,p in expected.items():
  f=current.get(key)
  if not f or f.get('Hashes',{}).get('md5','').lower()!=md5(p):bad.append(key)
 extras=[key for key in current if key.startswith(('Trainer Slides/','Learner Slides/','Learner Guide/','Lesson Plan/','Activities/')) and key not in expected]
 if bad or extras:raise RuntimeError('Missing/mismatched='+repr(bad)+' extra current='+repr(extras))
 preserved=json.loads(Path('/tmp/C818-preserved-drive-before.json').read_text())
 for folder,rows in preserved.items():
  now={f['Path'].removeprefix(folder+'/'):f for f in files if f['Path'].startswith(folder+'/')}
  if set(now)!={f['Path'] for f in rows}:raise RuntimeError('Preserved folder inventory changed: '+folder)
  for f in rows:
   n=now.get(f['Path'])
   if not n or n['ID']!=f['ID'] or n.get('Hashes')!=f.get('Hashes'):raise RuntimeError('Preservation mismatch: '+folder+'/'+f['Path'])
 print('Drive verified:',len(expected),'current files with matching MD5; no extra active courseware/labs; brochure and trainer resources preserved')
 return current,expected
if __name__=='__main__':
 c,e=verify_drive();out=Path('/tmp/C818-drive-verified.json');out.write_text(json.dumps(c,indent=2));os.chmod(out,0o600)

# Anonymous file downloads provide stronger evidence than HTTP 200 viewer pages.
def verify_anonymous(current,expected):
 checks=[]
 for path,local in expected.items():
  if path.startswith('Activities/'):continue
  fid=current[path]['ID'];url='https://drive.usercontent.google.com/download?id='+fid+'&export=download&confirm=t'
  req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0 C818 courseware verification'})
  with urllib.request.urlopen(req,timeout=60) as response:body=response.read()
  actual=hashlib.md5(body).hexdigest()
  if actual!=md5(local):raise RuntimeError('Anonymous download mismatch: '+path)
  checks.append(path)
 print('Anonymous downloads verified:',len(checks),'editable and PDF courseware files')
 return checks

def verify_storefront(current):
 spec=importlib.util.spec_from_file_location('courseware_api','/Users/alfredang/.agents/skills/non-wsq-lms-push/lms_push_nonwsq.py')
 module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
 after=module.api('GET',sku='C818');before=json.loads(Path('/tmp/C818-storefront-before.json').read_text())
 managed={'trainer_slides_url','learner_slides_url','lesson_plan_url','learner_guide_url','lab_url','courseware_link'}
 fields=after['courseware']
 for field,prefix,suffix in [('trainer_slides_url','Trainer Slides/','.pptx'),('learner_slides_url','Learner Slides/','.pdf'),('lesson_plan_url','Lesson Plan/','.pdf'),('learner_guide_url','Learner Guide/','.pdf')]:
  files=[f for path,f in current.items() if path.startswith(prefix) and path.endswith(suffix)]
  if len(files)!=1 or files[0]['ID'] not in fields.get(field,''):raise RuntimeError('Storefront mismatch: '+field)
 if '1jsJ5mEIYixfBusNYpmUsG1y4p7E4iVdC' not in fields['lab_url'] or ROOT not in fields['courseware_link']:raise RuntimeError('Wrong course/lab folder')
 for k,v in before['courseware'].items():
  if k not in managed and fields.get(k)!=v:raise RuntimeError('Unmanaged field changed: '+k)
 for k in ['sku','product_id','name']:
  if after.get(k)!=before.get(k):raise RuntimeError('Course identity changed: '+k)
 print('Storefront verified: six current links; identity and brochure preserved')
 out=Path('/tmp/C818-storefront-after.json');out.write_text(json.dumps(after,indent=2));os.chmod(out,0o600)
 return after
