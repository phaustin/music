from pythonlibs.pyutils import walker
from pythonlibs.pyutils.named_tup import namedtuple
from pythonlibs.pyutils.md5sum import md5sum

import stat
dsw=walker.DirectoryStatWalker
basedir='/home/phil/mirrors'
keepfiles=[]
for fileitem in dsw(basedir):
    if not fileitem['isDir']:
        filesize=fileitem['fullStats'][stat.ST_SIZE]
        try:
            filename=fileitem['filename']
            fullname=fileitem['fullname']
        except:
            print fileitem['fullname']
            continue
        thetup=namedtuple('thefile','filename filesize fullname')
        filetup=thetup(filename=filename,
                       filesize=filesize,
                       fullname=fullname)
        keepfiles.append(filetup)

import hashlib

for item in keepfiles[:100]:
    print item.fullname.decode('latin1')
    print md5sum(item.fullname)
    

