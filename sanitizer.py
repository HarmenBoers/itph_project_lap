import musicbrainzngs
import re
import unicodedata
import az_scraper as az


musicbrainzngs.set_useragent(
    "python-musicbrainzngs-example",
    "0.1",
    "https://github.com/alastair/python-musicbrainzngs/",
)


def get_song_names(artist_dict):
    '''
    This function takes an artist dictioanry as supplied by the MusicBrainz API
    :param artist_dict: dictionary as retreived from musicbrainz api
    :return: dictionary of song names from artist
    '''
    artist_dict = {}
    # Do STUFF with the song names
    artists = ['Caro Emerald']
    song_names = {}

    #Only test code can be commented out when we use artist_songs.py
    for a in artists:
        artist_dict[a] = musicbrainzngs.search_recordings(artist=a, limit=25)

    #For all artists get the song names
    for a in artists:
        print(artist_dict)
        for recording in artist_dict[a]['recording-list']:
            song_name = recording['title']
            print(song_name)
            if a in song_names:
                song_names[a].append(song_name)
            else:
                song_names[a] = [song_name]
        print(song_names)
    print("###################")
    return song_names


def get_sanitized_dict(song_names):
    '''
    This function makes a sanitized dictionary and attempts to remove all duplicate songs, also removes accents from letters
    :param song_names: the dictionary from get_song_names
    :return: a dictionary with artist as a key and no duplicate songs
    '''
    print('santizing dictionary')
    sanitized_dict = {}
    checklist = []

    for k in song_names:
        for s in set(song_names[k]):
            s = strip_accents(s)
            check = alpha_numeric(s)
            if check not in checklist:
                if k in sanitized_dict:
                    sanitized_dict[k].append(s)
                else:
                    sanitized_dict[k] = [s]
                checklist.append(check)

    print(sanitized_dict)
    return sanitized_dict


def get_url_dict(sanitized_dict):
    '''
    This function takes a dictionary from get_sanitized_dict
    :param sanitized_dict: the result from the get_sanitized function (song list with no duplicates)
    :return: a dictionary with artist keys and song urls to AZLyrics.com
    '''
    print('##############')
    print('Making urls')
    url_dict = {}
    #Create a dictionary with all urls  required to scrape the lyrics of a song.
    for k in sanitized_dict:
        for song in sanitized_dict[k]:
            sanitized_artist = alpha_numeric(k)
            lyric_url = 'http://www.azlyrics.com/lyrics/' + sanitized_artist + '/' + alpha_numeric(song) + '.html'
            if k in url_dict:
                url_dict[k].append(lyric_url)
            else:
                url_dict[k] = [lyric_url]
    print(url_dict)
    # for k in url_dict:
    #     for url in url_dict[k]:
    #         db.db_store(az.Scraper(url))
    return url_dict


def strip_brackets(song_name):
    if '(' in song_name:
        until = song_name.index('(')
        song_name = song_name[:until]
    return song_name


def alpha_numeric(s):
    return re.sub('[^a-zA-Z0-9]', "", s).lower()


def strip_accents(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')


get_url_dict(get_sanitized_dict(get_song_names()))


# scr.get_song_info()
