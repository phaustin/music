from pyutils.util import DirectoryStatWalker as dsw
import os,stat
from collections import defaultdict
from pyutils.named_tup import namedtuple
import sqlalchemy as sql

if __name__== "__main__":
    music_dirs=['/home/phil/Music_kathy','/home/phil/Music',\
                '/home/phil/phtransfer/My Documents/My Music/newmusic',\
                '/home/phil/phtransfer/My Documents/cdproj',\
                '/home/phil/mirrors']
    import os
    keepfiles=[]
    #
    # dictionary keyed by file suffix containing all
    # the files with that suffix
    #
    listdict=defaultdict(list)
    thetup=namedtuple('thefile','filename filesize fullname')
    for the_dir in music_dirs:
        for fileitem in dsw(the_dir):
            if not fileitem['isDir']:
                filesize=fileitem['fullStats'][stat.ST_SIZE]
                filename=unicode(fileitem['filename'])
                fullname=unicode(fileitem['fullname'])
                filetup=thetup(filename=filename,
                               filesize=filesize,
                               fullname=fullname)
                keepfiles.append(filetup)
                head,tail=os.path.splitext(filename)
                listdict[tail[1:].lower()].append(filetup)

    db = sql.create_engine('sqlite:///songs.db')
    db.echo = False  # Try changing this to True and see what happens
    metadata = sql.MetaData(db)

    songs = sql.Table('songs', metadata,
        sql.Column('song_id', sql.Integer, primary_key=True),
        sql.Column('filename', sql.Unicode(16)),
        sql.Column('fullname', sql.Unicode(16)),
        sql.Column('filesize', sql.Integer),
        sql.Column('filetype', sql.Unicode(16)),
    )

    try:
        db.drop(songs)
    except:
        pass

    songs.create(checkfirst=False)
    insert=songs.insert()

    music_types=['m4a','wma','flac','mp3','m4p']
    type_dict=defaultdict(list)
    for the_type in music_types:
        print the_type,len(listdict[the_type])
        for song_tup in listdict[the_type]:
            insert.execute(filename=song_tup.filename,
                           fullname=song_tup.fullname,
                           filesize=song_tup.filesize,
                           filetype=the_type)
    


    
    ## for song in listdict[the_type]:
        
    ##     thetup=namedtuple('filename'=song.filename,
    ##                       'filesize'=song.filesize)
        
    
                
                

                    


            

        
