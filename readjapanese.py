import mutagen
from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
import sqlalchemy as sql
from sqlalchemy.orm import mapper,create_session
import string,os,shutil,pickle
import fnmatch

m3ufile='/home/phil/Music/japaneseb.m3u'
infile=open(m3ufile,'r')
allsongs=infile.readlines()

import enchant
d = enchant.Dict("en_US")
from enchant.tokenize import get_tokenizer
tknzr = get_tokenizer("en_US") 

for count,item in enumerate(allsongs):
    if fnmatch.filter([item], '*mirrors*'):
        audio = EasyID3(item.strip())
        print "filename=",item.strip()
        print 'album=',audio['album'][0]
        print 'artist=',audio['artist'][0]
                
## for item in results:
##     print item
##     oldfile=item[2]
##     print "target: ",oldfile
##     newfile=string.join(oldfile.split('/')[3:],'/')
##     newdir,tail=os.path.split(newfile)
##     try:
##         os.makedirs(newdir)
##     except OSError:
##         pass
##     shutil.copyfile(oldfile,newfile)
##     print oldfile, newfile

## for item in results:
##     try:
##         bob = EasyID3(item[2])
##         print "fullname success: ",item[2]
##         for key in bob.keys():
##             print key,bob[key]
##     except mutagen.id3.ID3NoHeaderError:
##         print 'failed ',item[2]
