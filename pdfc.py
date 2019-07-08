#!/usr/bin/python
# -*- coding: utf-8 -*-
# in DOS: set PYTHONIOENCODING=utf-8
import sys
import PyPDF2, traceback
from subprocess import check_output
from re import sub
def debug(msg):
    #print(msg)
    pass
if sys.version_info[0] == 2:
    reload(sys)
    sys.setdefaultencoding('utf8')
    py = 2
else:
    py = 3
try :
    src = sys.argv[1]
except :
    src = r'tmp.pdf'
offs=int(sys.argv[2]) if len(sys.argv) > 2 else 0
input1 = PyPDF2.PdfFileReader(open(src, "rb"))
nPages = input1.getNumPages()
page = 0
for i in range(nPages) :
    page += 1
    page0 = input1.getPage(i)
    mbox = page0['/MediaBox']
    try :
        for annot in page0['/Annots'] :
            ann0 = annot.getObject()       # 
            if ann0['/Type'] == '/Annot' and ann0['/Subtype'] != '/Popup':
                if offs==0:
                    pno = "p. "+str(page)+": "
                else:
                    pno = "p. "+str(page-offs)+"("+str(page)+"): "
                debug(ann0)
                comm = ann0['/Contents']
                if ann0['/Subtype'] == '/Text':
                    context = ''
                else:
                    rect=ann0['/Rect']
                    s = 'pdftotext -f %d -l %d -x %d -y %d -H %d -W %d %s -'
                    s = s%(page, page, rect[0], mbox[3]-rect[3], rect[3]-rect[1], rect[2]-rect[0],src)
                    debug(s)
                    c = s.split()
                    context = check_output(c)
                    if py == 3:
                        context = context.decode('utf-8')
                    debug(context)
                    #import pdb; pdb.set_trace()
                    context = context.replace('\f','')
                    context = context.replace('\b','')
                    context = context.replace('\r','')
                    context = context.replace('\n',' ')
                    context = sub('\s+',' ',context)
                    context=context.rstrip()
                    debug(context)
                    #context = 'falta puxar o contexto – '
                    context += ' – '
                if py == 2:
                    print(unicode(pno+context+comm))
                else:
                    print(pno+context+comm)
    except : 
        # there are no annotations on this page
        pass
