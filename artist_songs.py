__author__ = 'Harme'
import musicbrainzngs
import sys

musicbrainzngs.set_useragent(
    "python-musicbrainzngs-example",
    "0.1",
    "https://github.com/alastair/python-musicbrainzngs/",
)


class Songloader():

    def __init__(self, artists):
        self.artists = artists
        self.artist_dict = self.get_artist_info(artists)

    # self.sanitized_songs = self.sanitize_song_names(self.artist_dict)

    
    def get_artist_info(self, artists):
        '''
        This function uses the musicbrainz API and takes a list of artist names and finds the songs they made / sung etc.
        :param artists: list of artist names
        :return: dictionary with artist name as a key and a dictionary of songs with metadata about the song
        '''
        artist_dict = {}
        # Get the first results and put in dictionary (required to get teh recording count
        for a in artists:
            artist_dict[a] = musicbrainzngs.search_recordings(artist=a, limit=25)
        print(artist_dict)

        # Now find all the songs for each artist based on the offset gained from the recording count variable
        for a in artists:
            #recording_count = artist_dict[a]['recording-count']
            #For testing
            recording_count = 51
            offs = 25

            # While songs are left keep appending them to the recording-list
            while recording_count > 0:
                for i in range(divmod(recording_count, 25)[0] + 1):
                    print(i)
                    fetch = musicbrainzngs.search_recordings(artist=a, recording='22', limit=25, offset=offs)
                    artist_dict[a]['recording-list'] += fetch['recording-list']
                    offs += 25
                    recording_count -= 25

        # For testing purposes only
        f = open('caro_dict.txt', 'w')
        # f.write(str(artist_dict))
        # f.close()
        # print(artist_dict)
        return artist_dict


if __name__ == '__main__':
    Songloader(["taylor swift"])
# caro =
# sanitize(caro)
