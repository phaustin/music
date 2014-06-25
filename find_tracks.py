#!/usr/bin/env /Users/phil/miniconda3/bin/python
# -*- coding: utf-8 -*-
"""
    find_tracks.py /Volumes/green1/mirrors/cdproj/various_artists/the_civil_war wR2Ep0GXwXTg4Ue9XCxx6k0Yv6E-
"""
from __future__ import  print_function
import glob,sys,os
import argparse, textwrap
import musicbrainzngs


def make_key(filename=None,track=None):
    if filename:
        filename,ext=os.path.splitext(filename)
    else:
        filename=track['artist-credit-phrase'] + track['recording']['title']
    out=filename.replace('_','').lower()
    out=out.replace(' ','')
    out=out.replace('(','')
    out=out.replace(')','')
    out=out.replace("'",'')
    out=out.replace("&",'')
    return out[:4] + out[-10:]

def strip_result(discid):
    result = musicbrainzngs.get_releases_by_discid(discid,includes=["labels","recordings","artist-credits"])
    track_list=result['disc']['release-list'][0]['medium-list'][0]['track-list']
    disc_title=result['disc']['release-list'][0]['title']
    out=[]
    for track in track_list:
        title=track['recording']['title']
        item=dict(artists=track['artist-credit-phrase'],
                num=track['number'],
                title=title,
                key=make_key(track=track))
        out.append(item)
    return disc_title,out
                 
if __name__=='__main__':

    linebreaks=argparse.RawTextHelpFormatter
    descrip=textwrap.dedent(globals()['__doc__'])
    parser = argparse.ArgumentParser(formatter_class=linebreaks,description=descrip)
    linebreaks=argparse.RawTextHelpFormatter
    parser.add_argument('album', type=str,help='path with wildcards')
    parser.add_argument('discid', type=str,help='musicbrainz disc id')

    args=parser.parse_args()
    print("arrived: args are {}".format(args))
    #
    #  make a list of (key,filename) tuples for each mp3 file
    #  format is first 4 charaters of artist + last 10 characters of title
    #
    for subdir, dirs, files in os.walk(args.album):
        key_list=[]
        for the_file in files:
            parts=the_file.split('_')
            #handle 26-jacqueline_schwab__battle_cry_of_freedom.mp3
            tracknum=parts[0].split('-')
            if len(tracknum) > 1:
                try:
                    int(tracknum[0])
                    print("skipping explicitly assigned {}".format(the_file))
                    continue
                except ValueError:
                    print("found non-integer in front of filename for {}".format(the_file))
                    raise ValueError
            key_list.append((the_file,make_key(filename=the_file)))
            dup_set=set([x for x in key_list if key_list.count(x) > 1])
        if len(dup_set) > 1:
            raise Exception("found dups: {}".format(repr(dup_set)))
        key_dict={the_tup[1]:the_tup[0] for the_tup in key_list}

                                

    disc_title,tracks=strip_result(args.discid)
    for the_track in tracks:
        the_track['filename']=key_dict[the_track['key']]
    out_dict=dict(title=disc_title,path=args.album,tracks=tracks,discid=args.discid)
    print(out_dict)



    
    


