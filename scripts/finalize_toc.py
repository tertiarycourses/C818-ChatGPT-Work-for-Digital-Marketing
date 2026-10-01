from pathlib import Path
import re,sys,fitz
from docx import Document

def norm(s):return re.sub(r'[^a-z0-9]','',s.lower())
def update(docx_path):
 p=Path(docx_path);doc=Document(p);pdf=fitz.open(p.with_suffix('.pdf'))
 heads=[para.text for para in doc.paragraphs if para.style.name in ('Heading 1','Heading 2') and para.text.strip()]
 toc_indices=[i for i,pg in enumerate(pdf) if len(re.findall(r'\.{8,}',pg.get_text()))>2]
 start=max(toc_indices)+1 if toc_indices else 3
 page_text=[norm(pg.get_text()) for pg in pdf];mapping={};cursor=start
 for h in heads:
  key=norm(h)
  hits=[i for i in range(cursor,len(pdf)) if key in page_text[i]]
  if not hits:raise RuntimeError('Heading not found: '+h)
  cursor=hits[0];mapping[h]=cursor+1
 changed=0
 for para in doc.paragraphs:
  if '\t' not in para.text:continue
  h=para.text.rsplit('\t',1)[0]
  if h in mapping:
   want=h+'\t'+str(mapping[h]);changed+=int(para.text!=want)
   # Preserve paragraph layout and run styling.
   if para.runs:para.runs[0].text=want
   for run in para.runs[1:]:run.text=''
 doc.save(p);print(p.name,'mapped',len(mapping),'headings; corrected',changed)
 return mapping
if __name__=='__main__':
 for p in sys.argv[1:]:update(p)
