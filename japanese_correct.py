from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3

filename=list()
album=list()
artist=list()
filename.append( "/home/phil/mirrors/emusic/Sonny Rollins/+3/Sonny Rollins_+3_04_Mona Lisa.mp3")
album.append( u'Mona Lisa')
artist.append( u'Sonny Rollins')
filename.append( "/home/phil/mirrors/emusic/Dar Williams/Dar Williams The Beauty Of The Rain 06 The One Who Knows Feat. Alison Krauss).mp3")
album.append( u'The Beauty of the Rain')
artist.append( u'Dar Williams')
filename.append( "/home/phil/mirrors/emusic/Dar Williams/Dar Williams The Beauty Of The Rain 09 Whispering Pines Feat. Steffan Lessard, Chris Botti, Cliff Eberh.mp3")
album.append( u'The Beauty of the Rain')
artist.append( u'Dar Williams')
filename.append( "/home/phil/mirrors/emusic/Jeno Jando/BEETHOVEN_ Piano Sonatas Nos 14, 21 and 23/Jeno Jando_BEETHOVEN_ Piano Sonatas Nos 14, 21 and 23_01_Piano Sonata No. 14_ Adagio sostenuto.mp3")
album.append( u'Beethoven Piano Sonatas Nos 14, 21 and 23')
artist.append( u'Jeno Jando')
filename.append( "/home/phil/mirrors/emusic/Liona Boyd/Liona Boyd The Best Of Liona Boyd 11 Jesu, Joy of Man's Desiring (Bach).mp3")
album.append( u'The Best Of Liona Boyd')
artist.append( u'Liona Boyd')
filename.append( '/home/phil/mirrors/emusic/Dexter Gordon/The Complete Prestige Recordings/Dexter Gordon_The Complete Prestige Recordings_05_In A Sentimental Mood.mp3')
album.append( u'The Complete Prestige Recordings')
artist.append( u'Dexter Gordon')
filename.append( "/home/phil/mirrors/emusic/Ludwig Van Beethoven/Immortal Beethoven/Ludwig Van Beethoven_Immortal Beethoven_02_Bagatelle In A Minor 'Fur Elise'.mp3")
album.append( 'Immortal Beethoven')
artist.append( 'Bagatelle')
filename.append( '/home/phil/mirrors/emusic/Ludwig Van Beethoven/Immortal Beethoven/Ludwig Van Beethoven_Immortal Beethoven_04_Adagio sostenuto.mp3')
album.append( 'Immortal Beethoven')
artist.append( 'Adagio')
filename.append( "/home/phil/mirrors/emusic/Ludwig Van Beethoven/Immortal Beethoven/Ludwig Van Beethoven_Immortal Beethoven_08_Adagio cantabile.mp3")
album.append( 'Immortal Beethoven')
artist.append( 'Canatabile')
filename.append( "/home/phil/mirrors/emusic/Sally Harmon/Sally Harmon Let It Snow! 07 We're Walking In The Air.mp3")
album.append( u'Let it Snow')
artist.append( u'Sally Harmon')
filename.append( "/home/phil/mirrors/emusic/Various Artists - The Secret Mountain _ Virtual/Various Artists - The Secret Mountain _ Virtual Dream Songs Night Songs From China to Senegal 12 All the pretty horses.mp3")
album.append( 'Virtual Dream Songs Night Songs From China to Senegal')
artist.append('Unknown')
filename.append( "/home/phil/mirrors/emusic/Gloria Sklerov/Gloria Sklerov Set Your Wedding To Music 15 Pachelbel's Cannon In D-I.mp3")
album.append( u'Set Your Weeding To Music')
artist.append( u'Unknown')
filename.append( "/home/phil/mirrors/emusic/Dexter Gordon/The Complete Prestige Recordings/Dexter Gordon_The Complete Prestige Recordings_02_Misty.mp3")
album.append( "Dexter Gordon_The Complete Prestige Recordings")
artist.append( "Dexter Gordon")
filename.append( "/home/phil/mirrors/emusic/Dar Williams/Dar Williams My Better Self 02 I'll Miss You Till I Meet You.mp3")
album.append( u"My Better Self")
artist.append( u"Dar Williams")
filename.append( "/home/phil/mirrors/emusic/Dar Williams/Dar Williams My Better Self 06 Two Sides Of The RIver.mp3")
album.append( u"My Better Self")
artist.append( u"Dar Williams")
filename.append( "/home/phil/mirrors/emusic/Dar Williams/Dar Williams End Of The Summer 07 My Friends.mp3")
album.append( u"My Better Self")
artist.append( u"Dar Williams")
filename.append( "/home/phil/mirrors/emusic/Dar Williams/Dar Williams Mortal City 09 The Blessings.mp3")
album.append( u"My Better Self")
artist.append( u"Dar Williams")
filename.append( "/home/phil/mirrors/emusic/Dar Williams/Dar Williams My Better Self 09 So Close To My Heart.mp3")
album.append( u"My Better Self")
artist.append( u"Dar Williams")
filename.append( "/home/phil/mirrors/emusic/Dar Williams/Dar Williams The Honesty Room 11 I Love, I Love (Traveling II).mp3")
album.append( u"My Better Self")
artist.append( u"Dar Williams")
filename.append( "/home/phil/mirrors/emusic/Dar Williams/Dar Williams My Better Self 12 You Rise And Meet The Day.mp3")
album.append( u"My Better Self")
artist.append( u"Dar Williams")
filename.append( "/home/phil/mirrors/emusic/Dar Williams/Dar Williams The Honesty Room 13 Arrival.mp3")
album.append( u"My Better Self")
artist.append( u"Dar Williams")
filename.append( "/home/phil/mirrors/emusic/Dar Williams/Dar Williams Out There Live 17 TheBabysitter's Here Intro.mp3")
album.append( u"My Better Self")
artist.append( u"Dar Williams")
filename.append( "/home/phil/mirrors/emusic/Dar Williams/Dar Williams Out There Live 18 The Babysitter's Here.mp3")
album.append( u"My Better Self")
artist.append( u"Dar Williams")
filename.append( "/home/phil/mirrors/emusic/Michael Allen Harrison/Michael Allen Harrison Bedtime Lullabies 08 All The Pretty Little Horses, All The World Is Sleeping.mp3")
filename.append("/home/phil/mirrors/emusic/Sally Harmon/Snap, Classical, Pop II!/Sally Harmon_Snap, Classical, Pop II!_03_Fur Elise.mp3")
album.append(u"Classical Pop II")
artist.append(u"Sally Harmon")
filename.append("/home/phil/mirrors/emusic/Dar Williams/Dar Williams Mortal City 02 February.mp3")
album.append( u"Mortal City")
artist.append( u"Dar Williams")
filename.append("/home/phil/mirrors/emusic/Dar Williams/Dar Williams Mortal City 07 Family.mp3")
album.append( u"Mortal City")
artist.append( u"Dar Williams")
album.append( u"Bedtime Lullabies")
artist.append( u"Michael Allen Harrison")
print len(filename),len(album),len(artist)
for count,the_file in enumerate(filename):
    audio = EasyID3(the_file.strip())
    audio['album'] = album[count]
    audio['artist'] = artist[count]
    audio.save()


