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
import pickle


if __name__== "__main__":
    picfile=open('albums.pic','r')
    albums=pickle.load(picfile)
    picfile.close()
    db = sql.create_engine('sqlite:///songs.db')
    db.echo = False # Try changing this to True and see what happens
    metadata = sql.MetaData(db)
    songs = sql.Table('songs', metadata, autoload=True)
    s=songs.select(songs.c.filetype=='mp3')
    for album in albums:
        for track in album['tracks']:
            values=track.split('/')
            if  len(values) ==3:
                searchstring="%%%s/%s%%" % tuple(values[1:])
                out=s.where(songs.c.fullname.like(searchstring))
                test=out.execute()
                if len(test.fetchall()) ==0:
                    print track,album['album']


