import mutagen
from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
import sqlalchemy as sql
from sqlalchemy.orm import mapper,create_session
import string,os,shutil,pickle
import glob

thefiles=glob.glob('/home/phil/mirrors/TTRH-1-Weather/*')

for a_file in thefiles:
    try:
        bob = EasyID3(a_file)
        print "fullname success: ",a_file
        for key in bob.keys():
            print key,bob[key]
    except mutagen.id3.ID3NoHeaderError:
        print 'failed ',a_file
