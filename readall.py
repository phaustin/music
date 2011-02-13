from pyutils.util import DirectoryStatWalker as dsw
from pyutils.process import command 
from pyutils.named_tup import namedtuple

import os,stat
from collections import defaultdict
from pyutils.named_tup import namedtuple
import sqlalchemy as sql
from sqlalchemy.orm import mapper,create_session
import mutagen
from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
import shlex

class Songs(object):
    pass
tse
if __name__== "__main__":
    db = sql.create_engine('sqlite:///songs.db')
    db.echo = True # Try changing this to True and see what happens
    metadata = sql.MetaData(db)
    songs = sql.Table('songs', metadata, autoload=True)
    s=songs.select(songs.c.filetype=='mp3')
    ## out=s.where(songs.c.fullname.like('%donald_and_lydia.mp3%'))
    ## test=out.execute()
    ## test.fetchall()
    rs=s.execute()
    out=rs.fetchall()
    songmapper=mapper(Songs,songs)
    session=create_session()
    ## out = session.query(Songs).select(songs.c.filetype=='mp3')
    good_mp3s=[]
    bad_mp3s=[]
    for item in out:
        fullname=item[2]
        try:
            print "debug: ",item[2]
            bob = EasyID3(fullname)
            good_mp3s.append(item)
        except:
            print "caught trouble"
            bad_mp3s.append(item)
    ## for item in bad_mp3s:
    ##     print item[2]
    ## for item in good_mp3s:
    ##     print item[2]
        ## new_file=the_file.replace('/home/phil/Music','/home/phil/mirrors')
        ## dirname,filename=os.path.split(new_file)
        ## try:
        ##     os.makedirs(dirname)
        ## except OSError:
        ##     pass
        ## the_command=r"""lame --preset extreme --id3v2-only  "%s" "%s" """ % (the_file,new_file)
        ## error,output=command(the_command)
        ## print "error on lame command: %s\n%s\n" % (the_file,error)

#
# get individual columns
#
## out=sql.select([songs.c.filetype,songs.c.filename])
## items=out.execute()
## for item in items:
##     print item
