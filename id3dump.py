#!/usr/bin/env /Users/phil/miniconda/bin/python
# -*- coding: utf-8 -*-
"""
    id3dump.py '/Users/phil/Music/iTunes/iTunes Media/Music/Iron & Wine'
"""
import glob,sys,os, json
import argparse, textwrap,mutagen
from mutagen.easymp4 import EasyMP4
from mutagen.mp3 import EasyMP3
from mutagen.mp4 import MP4
from collections import OrderedDict

import shlex, subprocess
from subprocess import Popen, PIPE, STDOUT

filters = ['m4a','mp3']

easy_fun=dict(m4a=EasyMP4,mp3=EasyMP3)

def command(command_line):
     """
     usage: status,output=command(commandstring)
     """
     args = shlex.split(command_line)
     p = Popen(args, stdout=PIPE, stderr=STDOUT, shell=True)
     s = p.stdout.read()
     return p.wait(), s


def proc_dir(path, force):
    print("arrived proc_dir, directory? ",os.path.isdir(path))
    test=os.walk(path)
    for subdir, dirs, files in os.walk(path):
        print("here is subdir: ",subdir)
        for the_file in files:
            main,exten=os.path.splitext(the_file)
            exten=exten[1:]
            print("spiit: ",main,exten)
            if exten in filters:
                proc_file('%s/%s' % (subdir, the_file), force, exten)

def proc_file(the_file, force, exten):
    print("this is the file: --{}--".format(the_file))
    output = "%s.json" % the_file

    if os.path.exists(output) and not force:
        print("'.json' file already exists, please use '-f' or '--force' option!")
        return

    fields = {}
    subfields = {}
    test=easy_fun[exten](the_file)
    print("here is test: ",test,exten)
    tags=['title','tracknumber','album','artist', 'genre','discnumber','albumsort', 'albumartist',  'artistsort', 'titlesort','date']
    out_dict=OrderedDict()
    for item in tags:
        if item in test:
            out_dict[item]=test[item]
    print(json.dumps(out_dict,indent=4))



if __name__=='__main__':

    linebreaks=argparse.RawTextHelpFormatter
    descrip=textwrap.dedent(globals()['__doc__'])
    parser = argparse.ArgumentParser(formatter_class=linebreaks,description=descrip)
    linebreaks=argparse.RawTextHelpFormatter
    parser.add_argument('wildcard', type=str,help='path with wildcards')
    parser.add_argument('--force', type=bool,default=False,help='overwrite json file')
    args=parser.parse_args()
    print("arrived: args are {}".format(args))
    print("epassing args.wildcard=",args.wildcard)
    print("and is it a file? ",os.path.isfile(args.wildcard))
    if os.path.isfile(args.wildcard):
        proc_file(args.wildcard, args.force,'mp3')
    else:
        proc_dir(args.wildcard, args.force)

    the_test= EasyMP3('/Volumes/green1/mirrors/2006__we_shall_overcome_the_seeger_sessions/my_oklahoma_home.mp3')
    print(the_test)
    title='/Users/phil/Music/iTunes/iTunes Media/Music/Compilations/Poet_ A Tribute To Townes Van Zandt/01 To Live Is To Fly.mp3'
    test2=EasyMP3(title)
    print(test2)
    title='/Users/phil/Music/iTunes/iTunes Media/Music/Benjamin Gibbard/Former Lives/03 Teardrop Windows.m4a'
    test3=EasyMP4(title)
    print test3
    
    
    
    


