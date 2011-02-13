from pyutils.util import DirectoryStatWalker as dsw
import os

if __name__== "__main__":
    music_dirs=['/home/phil/Music_kathy','/home/phil/Music',\
                '/home/phil/phtransfer/My Documents/My Music/newmusic',\
                '/home/phil/phtransfer/My Documents/cdproj',]
    import os
    keepfiles=[]
    for the_dir in music_dirs:
        for fileitem in dsw(the_dir):
            if fileitem['isDir']:
                os.chmod(fileitem['fullname'],0755)
            else:
                os.chmod(fileitem['fullname'],0644)

            

        
