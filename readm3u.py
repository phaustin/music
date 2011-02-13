import fnmatch
import os
import pickle

bob_matches = []
for root, dirnames, filenames in os.walk('/home/phil/m3udir'):
    for filename in fnmatch.filter(filenames, '*.m3u'):
        bob_matches.append(os.path.join(root, filename))

albums=[]
for item in bob_matches:
    head,tail = os.path.split(item)
    head,tail=os.path.splitext(tail)
    print head
    artist,album=head.split('-')
    entry={'artist':artist,'album':album}
    with open(item) as f:
        data = f.read().strip()
        tracks=data.split('\n')
        entry['tracks']=tracks
    albums.append(entry)

outfile=open('albums.pic','w')
pickle.dump(albums,outfile)
outfile.close()


    
## tracknumber [u'13']
## album [u'Atlantic Rhythm & Blues 1947-1974 Vol. 4 (1958-1962)']
## genre [u'General R&B']
## artist [u'Ben E. King']
## title [u'Spanish Harlem']
