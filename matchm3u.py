from pyutils.util import DirectoryStatWalker as dsw
from pyutils.named_tup import namedtuple
import string

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
import traceback as tb
import shutil


def command(command_line):
   """
   usage: status,output=command(commandstring)
   """ 
   from subprocess import Popen, PIPE, STDOUT
   args = shlex.split(command_line)
   p = Popen(args, stdout=PIPE, stderr=STDOUT, shell=False)
   s = p.stdout.read()
   return p.wait(), s

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
                results=test.fetchall()
                if len(results) ==0:
                    print "missing: ",track,album['album']
                elif len(results) !=1:
                    print len(results),results
                else:
                    oldfile=results[0][2]
                    print "solo track: ",oldfile
                    try:
                        bob = EasyID3(oldfile)
                        print "made it: "
                        for key in bob.keys():
                            print oldfile,key,bob[key]
                        newfile=string.join(oldfile.split('/')[3:],'/')
                        newdir,tail=os.path.split(newfile)
                        try:
                            os.makedirs(newdir)
                        except OSError:
                            pass
                        shutil.copyfile(oldfile,newfile)
                    except:
                        print "caught exception"
                        tb.print_exc()
                        newfile=string.join(oldfile.split('/')[3:],'/')
                        newdir,tail=os.path.split(newfile)
                        try:
                            os.makedirs(newdir)
                        except OSError:
                            pass
                        the_command=r"""lame --preset extreme --id3v2-only  "%s" "%s" """ % (oldfile,newfile)
                        the_command=unicode(the_command).encode("utf-8")
                        print "execute: ",the_command
                        error,output=command(the_command)
                        print "error on lame command: %s\n%s\n" % (output,error)

                            
                        
                    
                    


