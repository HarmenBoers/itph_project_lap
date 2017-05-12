__author__ = 'Harmen'

class Finder():
    def __init__(self):
        pass

    #Create a
    for a in artists:
        for song in sanitized_dict[a]:
            sanitized_artist = re.sub('[^a-zA-Z0-9]', "", a).lower()
            lyric_url = 'http://www.azlyrics.com/lyrics/' + sanitized_artist + '/' + song + '.html'
            if a in url_dict:
                url_dict[a].append(lyric_url)
            else:
                url_dict[a] = [lyric_url]
    print(url_dict)
    for k in url_dict:
        for url in url_dict[k]:
            scr.Scraper(url, True)
        # for artist_DICT
        # 	add sanitized name
        # 	check if name exists