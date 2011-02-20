import mutagen
from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
import sqlalchemy as sql
from sqlalchemy.orm import mapper,create_session
import string,os,shutil,pickle

db = sql.create_engine('sqlite:///songs.db')
db.echo=True
metadata = sql.MetaData(db)
songs = sql.Table('songs', metadata, autoload=True)
s=songs.select(songs.c.filetype=='mp3')
## searchstring="%%%s%%" % ('mirrors',)
## out2=out.where(songs.c.fullname.like(searchstring))
## test=out2.execute()
## thesongs=test.fetchall()


## s=songs.select()
## out=s.where(songs.c.fullname.like(searchstring))
## test=out.execute()
## results=test.fetchall()

picfile=open('albums.pic','r')
albums=pickle.load(picfile)
picfile.close()

albumtitle=u'luck_of_the_draw'

for count,item in enumerate(albums):
    firsthit=False
    if item['album'] == albumtitle:
        firsthit=True
        album=albums[count]
        break

tracks=album['tracks']


for count,track in enumerate(tracks):
    print "track: ",count + 1
    searchstring="%%%s%%" % ('mirrors',)
    out=s.where(songs.c.fullname.like(searchstring))
    searchstring="%%%s%%" % (albumtitle,)
    out2=out.where(songs.c.fullname.like(searchstring))
    test=out2.execute()
    head,tail=os.path.split(track)
    key,ext=os.path.splitext(tail)
    searchstring="%%%s%%" % (key,)
    out3=out2.where(songs.c.fullname.like(searchstring))
    test=out3.execute()
    thesongs=test.fetchall()
    print "hit: ",thesongs
    fullname=thesongs[0][2]
    audio = EasyID3(fullname)
    audio['tracknumber']=unicode('%d' % (count + 1),'utf-8')
    audio['album']=album['album']
    audio['artist']=album['artist']
    head,tail=os.path.split(track)
    title,ext=os.path.splitext(tail)
    audio['title']=title
    print "title: ",title
    audio.save()



        
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
