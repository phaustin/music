#!/usr/bin/env /Users/phil/miniconda/bin/python
# -*- coding: utf-8 -*-
"""
    b21dc704-d94d-4cb1-b9a0-dd80ed00e607
    find_tracks.py /Volumes/green1/mirrors/cdproj/various_artists/the_civil_war wR2Ep0GXwXTg4Ue9XCxx6k0Yv6E- --with_artists
    find_tracks.py /Volumes/green1/mirrors/cdproj/various/going_driftless_an_artists_tribute_to_greg_brown RpaUAm6QgqsVF9yEeQa4p0hxeUg-
    find_tracks.py /Volumes/green1/mirrors/cdproj/various/poet_a_tribute_to_townes_van_zandt b21dc704-d94d-4cb1-b9a0-dd80ed00e607
    python ~/repos/music/find_tracks.py /Volumes/green1/mirrors/warren_zevon/the_wind ssJYvpaz5qLHq26TEV84.68sXy4-
    find_tracks.py /Volumes/green1/mirrors/cdproj/various_artists/the_civil_war a6009187-f087-4bb7-9662-00b245d55825
"""
from __future__ import  print_function
import glob,sys,os
import argparse, textwrap
import musicbrainzngs
from mutagen.easymp4 import EasyMP4
from mutagen.mp3 import EasyMP3

musicbrainzngs.set_useragent(
    "python-musicbrainzngs-example",
    "0.1",
    "https://github.com/alastair/python-musicbrainzngs/",
)

def sanitize(the_string):
    out=the_string.replace('_','').lower()
    out=out.replace(' ','')
    out=out.replace('(','')
    out=out.replace(')','')
    out=out.replace("'",'')
    out=out.replace("&",'')
    out=out.replace(".",'')
    out=out.replace("/",'')
    out=out.replace(",",'')
    out=out.replace("?",'')
    out=out.replace("-",'')
    out=out.replace(":",'')
    out=out.replace('"','')
    out=out.replace(u'\u2019','')
    return out

def make_key_split(filename=None,track=None):
    if filename:
        filename,ext=os.path.splitext(filename)
        parts=filename.split('__')
        if len(parts) == 2:
            title,artist=parts
        else:
            title=parts[0]
    else:
        title=track['recording']['title']
    title=sanitize(title)
    return title[-5:]

def make_key_artists(filename=None,track=None):
    if filename:
        filename,ext=os.path.splitext(filename)
    else:
        filename=track['artist-credit-phrase'] + track['recording']['title']
    out=sanitize(filename)
    return out[:4] + out[-10:]


def make_key_tracknums(filename=None,track=None):
    """
       match track numbers
    """
    if filename:
        head,ext=os.path.splitext(filename)
        tracknum=head.split('-')
        tracknum=int(tracknum[1][:2])
    else:
        tracknum=int(track['number'])
    return tracknum


def make_key_titles(filename=None,track=None):
    if filename:
        filename,ext=os.path.splitext(filename)
    else:
        filename=track['recording']['title']
    out=sanitize(filename)
    return out[-4:]


def strip_result(id,make_key,disc_index):
    try:
        result = musicbrainzngs.get_releases_by_discid(id,includes=["labels","recordings","artist-credits"])
        root=result['disc']['release-list'][0]
        discid=result['disc']['id']
    except musicbrainzngs.ResponseError:
        result = musicbrainzngs.get_release_by_id(id,includes=["labels","recordings","artist-credits"])
        root=result['release']
        discid=None
        
    disc_count=root['medium-count']
    track_list=root['medium-list'][disc_index]['track-list']
    track_count=root['medium-list'][disc_index]['track-count']
    disc_title=root['title']
    release=root['id']

    out=[]
    for track in track_list:
        title=track['recording']['title']
        item=dict(artists=track['artist-credit-phrase'],
                num=track['number'],
                title=title,
                key=make_key(track=track))
        out.append(item)
    out_dict=dict(title=disc_title,track_count=track_count,path=the_album,track_list=out,discid=discid,
                  disc_count=disc_count,release=release)
    return out_dict

def make_track_dict(album_dict):
    track_num_dict={}
    for the_track in album_dict['track_list']:
        track_num_dict[int(the_track['num'])]=the_track
    album_dict['track_num_dict']=track_num_dict
    return None
                 
if __name__=='__main__':

    linebreaks=argparse.RawTextHelpFormatter
    descrip=textwrap.dedent(globals()['__doc__'])
    parser = argparse.ArgumentParser(formatter_class=linebreaks,description=descrip)
    linebreaks=argparse.RawTextHelpFormatter
    parser.add_argument('album', type=str,help='path with wildcards')
    parser.add_argument('id', type=str,help='musicbrainz discid or release id')
    parser.add_argument('--key_version',type=str,default='titles',help='titles,artists,tracknums or split')
    parser.add_argument('--disc_number',type=int,default=1,help='1, 2, etc.')
    parser.add_argument('--is_compilation',dest='compilation',action='store_true',help='true if album is various artists')
    args=parser.parse_args()
    print("arrived: args are {}".format(args))

    the_album=glob.glob(args.album)
    if len(the_album) != 1:
       raise Exception('glob of {} yields bad directory {}'.format(args.album,repr(the_album)))
    the_album=the_album[0]
    if not os.path.isdir(the_album):
        raise Exception('{} is not a directory'.format(the_album))
    #
    #  make a list of (key,filename) tuples for each mp3 file
    #  format is first 4 charaters of artist + last 10 characters of title
    #
    compilation=args.compilation
    print("compilation is set to: ",compilation)
    if args.key_version=='artists':
        make_key=make_key_artists
    elif args.key_version=='titles':
        make_key=make_key_titles
    elif args.key_version=='tracknums':
        make_key=make_key_tracknums
    elif args.key_version=='split':
        make_key=make_key_split
    else:
        raise ValueError('key version needs to be artists,titles, or tracknums')
    skip_tracks=[]
    disc_index=args.disc_number - 1
    for subdir, dirs, files in os.walk(the_album):
        print("walker found: {}".format(repr(files)))
        key_list=[]
        for the_file in files:
            name,ext=os.path.splitext(the_file)
            if ext not in ['.mp3','.m4a']:
                continue
            key_list.append((the_file,make_key(filename=the_file)))
            dup_set=set([x for x in key_list if key_list.count(x) > 1])
        if len(dup_set) > 1:
            raise Exception("found dups: {}".format(repr(dup_set)))
        key_dict={the_tup[1]:the_tup[0] for the_tup in key_list}

    album_dict=strip_result(args.id,make_key,disc_index)
    for the_track in album_dict['track_list']:
        try:
            the_track['filename']=key_dict[the_track['key']]
        except KeyError:
            print('missing {}'.format(repr(the_track)))
            the_track['filename']='Need Name'
    print(album_dict)
    print("files not assigned: ",skip_tracks)
    make_track_dict(album_dict)
    for the_track in skip_tracks:
        track_num,filename=the_track
        album_dict['track_num_dict'][track_num]['filename']=filename

    for track_num,the_track in album_dict['track_num_dict'].items():
        if the_track['filename']=='Need Name':
            print('skipping track: {}'.format(repr(the_track)))
            continue
        else:
            print(track_num,the_track)
        filename="{}/{}".format(album_dict['path'],the_track['filename'])
        mp3_file=EasyMP3(filename)
        print(filename)
        mp3_file['album']=album_dict['title']
        mp3_file['title']=the_track['title']
        if compilation:
            mp3_file['compilation']='1'
        mp3_file['artist']=the_track['artists']
        mp3_file['tracknumber']="{}/{}".format(track_num,album_dict['track_count'])
        mp3_file['discnumber']='{}/{}'.format(args.disc_number,album_dict['disc_count'])
        mp3_file.save()
        
#('here is test: ', {'album': [u'Poet: A Tribute To Townes Van Zandt'], 'artist': [u'John T. Van Zandt'], 'compilation': [u'1'], 'title': [u'My Proud Mountains'], 'encodedby': [u'iTunes 11.2.2'], 'composer': [u'Not Documented'], 'date': [u'2001'], 'tracknumber': [u'15/15'], 'discnumber': [u'1/1'], 'genre': [u'Country & Folk']}, 'mp3')
