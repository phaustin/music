import fnmatch
import os
import mutagen
from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3

print EasyID3.valid_keys.keys()

matches = []
for root, dirnames, filenames in os.walk('.'):
    for filename in fnmatch.filter(filenames, '*.mp3'):
        matches.append(os.path.join(root, filename))
print matches[:10]

good_matches = []
for root, dirnames, filenames in os.walk('Music'):
    for filename in fnmatch.filter(filenames, '*.mp3'):
        good_matches.append(os.path.join(root, filename))
print good_matches[:10]

bob_matches = []
for root, dirnames, filenames in os.walk('/home/phil/Music/Music/TTRH-1-Weather'):
    for filename in fnmatch.filter(filenames, '*.mp3'):
        bob_matches.append(os.path.join(root, filename))
print bob_matches[:10]

for bob_name in bob_matches:
    print '-'*60
    bob = EasyID3(bob_name)
    for key in bob.keys():
        print key,bob[key]
