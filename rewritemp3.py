import fnmatch
import os
import mutagen
from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
import shlex

def command(command_line):
   """
   usage: status,output=command(commandstring)
   """ 
   from subprocess import Popen, PIPE, STDOUT
   args = shlex.split(command_line)
   p = Popen(args, stdout=PIPE, stderr=STDOUT, shell=False)
   s = p.stdout.read()
   return p.wait(), s


print EasyID3.valid_keys.keys()

## date [u'2007']
## performer [u'Telmary']
## tracknumber [u'5']
## album [u'A Diario']
## genre [u'Hip-Hop']
## discnumber [u'1/1']
## artist [u'Los Van Van']
## title [u'Maril\xfa - Los Van Van']
## organization [u'DM Ahora']

def writefull(root,filenames):
    out=[os.path.join(root, filename) for filename in filenames]
    return out

good_mp3s = []
bad_mp3s = []
doublefiles = []
flacfiles = []
mp4files= []
mp3files = []
for root, dirnames, filenames in os.walk('/home/phil/mirrors/'):
    mp4files.extend(writefull(root,fnmatch.filter(filenames, '*.m4a')))
    mp3files.extend(writefull(root,fnmatch.filter(filenames, '*.mp3')))
    flacfiles.extend(writefull(root,fnmatch.filter(filenames, '*.flac')))
    doublefiles.extend(writefull(root,fnmatch.filter(filenames, '*.mp3.mp3')))
singlemp3s=set(mp3files).difference(set(doublefiles))
for fullname in singlemp3s:
    try:
        bob = EasyID3(fullname)
        for key in bob.keys():
            print "fullname success: ",key,bob[key]
        good_mp3s.append(fullname)
    except:
        bad_mp3s.append(fullname)

## for the_file in bad_mp3s:
##     new_file=the_file.replace('/home/phil/Music','/home/phil/mirrors')
##     dirname,filename=os.path.split(new_file)
##     try:
##         os.makedirs(dirname)
##     except OSError:
##         pass
##     the_command=r"""lame --preset extreme --id3v2-only  "%s" "%s" """ % (the_file,new_file)
##     error,output=command(the_command)
##     print "error on lame command: %s\n%s\n" % (the_file,error)


## tracknumber [u'13']
## album [u'Atlantic Rhythm & Blues 1947-1974 Vol. 4 (1958-1962)']
## genre [u'General R&B']
## artist [u'Ben E. King']
## title [u'Spanish Harlem']

