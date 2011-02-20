from pyutils.walker import DirectoryStatWalker as dswalk
import os
import fnmatch
from pyutils.process import command

for fileDict in dswalk("/home/phil/m3udir/"):
    thename=fileDict['fullname']
    if fnmatch.filter([thename], '*m3u'):
        with open(thename) as f:
            data = f.read()
            the_songs=data.split('\n')
            for song in the_songs:
            ## head,tail=os.path.split(thename)
            ## tail,ext=os.path.splitext(tail)
                command_string='locate %s'  %  song
                print command_string
                status,output=command(command_string)
                print status,output
        


