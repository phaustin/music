import mutagen
from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
import sqlalchemy as sql
from sqlalchemy.orm import mapper,create_session
import string,os,shutil,pickle
from mutagen.id3 import TPE2
import glob

tracks="/home/phil/mirrors/matthew_favorites/*mp3"
alltracks=glob.glob(tracks)
print alltracks

the_list=[]
for item in alltracks:
    try:
        album = EasyID3(item)
        print 60*'+'
        audio = mutagen.mp3.MP3(item)
        print len(audio.keys())
        audio['TPE2'] = TPE2(3, 'Various')
        print audio
        print audio.pprint()
        the_list.append(album['album'][0])
        album['album']=u"Matthew's favorites"
        album.save()
        if len(audio[u"COMM:CDDB:'eng'"].text) == 2:
            keep=audio[u"COMM:CDDB:'eng'"].text
            audio[u"COMM:CDDB:'eng'"].text=[keep[0]]
        audio.save()
    except mutagen.id3.ID3NoHeaderError:
        print 'failed ',item


## for count,track in enumerate(tracks):
##     print "track: ",count + 1
##     searchstring="%%%s%%" % ('mirrors',)
##     out=s.where(songs.c.fullname.like(searchstring))
##     searchstring="%%%s%%" % (albumtitle,)
##     out2=out.where(songs.c.fullname.like(searchstring))
##     test=out2.execute()
##     head,tail=os.path.split(track)
##     key,ext=os.path.splitext(tail)
##     searchstring="%%%s%%" % (key,)
##     out3=out2.where(songs.c.fullname.like(searchstring))
##     test=out3.execute()
##     thesongs=test.fetchall()
##     print "hit: ",thesongs
##     fullname=thesongs[0][2]
##     audio = EasyID3(fullname)
##     audio['tracknumber']=unicode('%d' % (count + 1),'utf-8')
##     audio['album']=album['album']
##     audio['artist']=album['artist']
##     head,tail=os.path.split(track)
##     title,ext=os.path.splitext(tail)
##     audio['title']=title
##     print "title: ",title
##     audio.save()



        
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
