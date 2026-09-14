"""Read-only checks for visible, per-unit H3 upload-order checklists."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
import argparse
import re

VOID = {'area','base','br','col','embed','hr','img','input','link','meta','param','source','track','wbr'}

class Document(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.nodes=[]; self.stack=[]

    def handle_starttag(self, tag, attrs):
        node={'tag':tag,'attrs':dict(attrs),'parents':self.stack.copy(),'text':[], 'index':len(self.nodes)}
        self.nodes.append(node)
        if tag not in VOID: self.stack.append(node)

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag,attrs)
        if tag not in VOID: self.stack.pop()

    def handle_endtag(self, tag):
        for i in range(len(self.stack)-1,-1,-1):
            if self.stack[i]['tag']==tag:
                del self.stack[i:];break

    def handle_data(self,data):
        for node in self.stack: node['text'].append(data)

def classes(node): return (node['attrs'].get('class') or '').split()
def descendant(node,parent): return any(x is parent for x in node['parents'])
def text(node): return ' '.join(''.join(node['text']).split())
def hidden(node):
    for x in node['parents']+[node]:
        a=x['attrs'];style=re.sub(r'\s+','',(a.get('style') or '').lower())
        if 'hidden' in a or a.get('aria-hidden')=='true' or 'display:none' in style or 'visibility:hidden' in style:return True
        if x['tag']=='details' and 'open' not in a:return True
    return False

def lint(path):
    path=Path(path).resolve();doc=Document();doc.feed(path.read_text(encoding='utf-8-sig'))
    units=[n for n in doc.nodes if n['tag']=='article' and 'h3-unit' in classes(n)]
    errors=[]
    if not units:return ['No h3-unit articles found']
    checklists=[n for n in doc.nodes if 'data-upload-unit' in n['attrs']]
    if len(checklists)!=len(units):errors.append('Expected one upload checklist per H3 unit')
    for n in checklists:
        if not any(descendant(n,u) for u in units):errors.append('Upload checklist is outside its unit')
    for unit in units:
        uid=unit['attrs'].get('data-h3-unit') or 'unnamed-unit'
        checks=[n for n in checklists if descendant(n,unit)]
        if len(checks)!=1:
            errors.append(f'{uid}: missing or duplicate upload checklist');continue
        box=checks[0]
        if box['attrs'].get('data-upload-unit')!=uid:errors.append(f'{uid}: checklist unit ID mismatch')
        if hidden(box):errors.append(f'{uid}: upload checklist is hidden or collapsed')
        prompts=[n for n in doc.nodes if descendant(n,unit) and ('prompt-block' in classes(n) or 'data-prompt-lang' in n['attrs'])]
        if not prompts:errors.append(f'{uid}: missing prompt block')
        elif box['index']>=min(n['index'] for n in prompts):errors.append(f'{uid}: checklist must precede prompts')
        rows=[n for n in doc.nodes if descendant(n,box) and 'data-upload-kind' in n['attrs']]
        if prompts and rows and max(n['index'] for n in rows)>=min(n['index'] for n in prompts):errors.append(f'{uid}: upload rows must precede prompts')
        slots={'image':[], 'video':[], 'audio':[]};rank=-1
        for row in rows:
            a=row['attrs'];kind=a.get('data-upload-kind');label=f'{uid}/{kind}'
            if kind not in slots:
                errors.append(f'{label}: invalid modality');continue
            order=['image','video','audio'].index(kind)
            if order<rank:errors.append(f'{uid}: modality groups out of order')
            rank=order
            try: slot=int(a.get('data-slot',''))
            except ValueError:slot=0
            slots[kind].append(slot)
            name=a.get('data-filename') or '';role=a.get('data-role') or '';visible=text(row)
            if hidden(row):errors.append(f'{label}: hidden upload row')
            if not name or name not in visible:errors.append(f'{label}: exact filename must be visible')
            if not role or role not in visible:errors.append(f'{label}: named role must be visible')
            prefix={'image':'图片','video':'视频','audio':'音频'}[kind]
            if not re.search(re.escape(prefix)+r'\s*'+str(slot)+r'(?!\d)',visible):errors.append(f'{label}: upload number must be visible')
            anchors=[n for n in doc.nodes if n['tag']=='a' and descendant(n,row) and name and name in text(n)]
            if len(anchors)!=1:
                errors.append(f'{label}: exact filename needs one working file link');continue
            href=anchors[0]['attrs'].get('href') or '';url=urlsplit(href)
            if not href or href.startswith('#') or url.scheme not in ('','file','http','https'):
                errors.append(f'{label}: invalid asset link')
            elif url.scheme not in ('http','https'):
                raw=unquote(url.path)
                if url.scheme=='file' and re.match(r'^/[A-Za-z]:/',raw):raw=raw[1:]
                f=Path(raw)
                if not f.is_absolute():f=path.parent/f
                if not f.is_file():errors.append(f'{label}: local asset missing: {name}')
                if f.name!=name:errors.append(f'{label}: linked filename differs from upload filename')
            if kind=='audio':
                target=a.get('data-target') or ''
                if not target or target not in visible:errors.append(f'{label}: audio target must be visible')
                if a.get('data-audio-mode') not in ('audio reference','audio reuse'):errors.append(f'{label}: invalid audio purpose')
                if a.get('data-model-label')!=f'<Audio {slot}>':errors.append(f'{label}: audio slot-label mismatch')
        for kind,values in slots.items():
            if values!=list(range(1,len(values)+1)):errors.append(f'{uid}/{kind}: slots must run from 1 in upload order')
        if not slots['image'] and not slots['video']:
            reason=box['attrs'].get('data-no-visual-inputs') or ''
            if not reason or reason not in text(box):errors.append(f'{uid}: visual references missing without visible reason')
    return errors

def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('html_file',type=Path);args=parser.parse_args()
    try:errors=lint(args.html_file)
    except (OSError,ValueError) as exc:print(f'FAIL: {exc}');return 2
    for error in errors:print('FAIL: '+error)
    if not errors:print('PASS: every unit has an expanded ordered upload checklist with visible linked filenames and roles')
    return int(bool(errors))

if __name__=='__main__':raise SystemExit(main())
