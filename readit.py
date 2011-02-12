import fnmatch
import os
import mutagen
from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3

print EasyID3.valid_keys.keys()



bob_matches = []
for root, dirnames, filenames in os.walk('/home/phil/Music/yoyo_ma/the_cello_suites_inspired_by_bach_disc_1'):
    for filename in fnmatch.filter(filenames, '*.mp3'):
        bob_matches.append(os.path.join(root, filename))

## tracknumber [u'13']
## album [u'Atlantic Rhythm & Blues 1947-1974 Vol. 4 (1958-1962)']
## genre [u'General R&B']
## artist [u'Ben E. King']
## title [u'Spanish Harlem']

for bob_name in bob_matches:
    try:
        print 'bob_name: ',bob_name,'-'*60
        bob = EasyID3(bob_name)
        for key in bob.keys():
            print key,bob[key]
    except:
        pass
