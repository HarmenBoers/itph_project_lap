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
		self.artist_dict = self.read_db(artists)
		#self.sanitized_songs = self.sanitize_song_names(self.artist_dict)

	def read_db(self, artists):
		result = {}

		#Get the first results and put in dictionary (required to get teh recording count
		for a in artists:
			result[a] = musicbrainzngs.search_recordings(artist=a, limit=25)
		print(result)

		#Now find all the songs for each artist based on the offset gained from the recording count variable
		for a in artists:
			recording_count = result[a]['recording-count']
			offs = 25

			#While songs are left keep appending them to the recording-list
			while recording_count > 0:
				for i in range(divmod(recording_count, 25)[0]+1):
					print(i)
					fetch = musicbrainzngs.search_recordings(artist=a, limit=25, offset=offs)
					result[a]['recording-list'] += fetch['recording-list']
					offs += 25
					recording_count -= 25

		# For testing purposes only
		f = open('caro_dict.txt', 'w')
		# f.write(str(result))
		# f.close()
		#print(result)
		return result

if __name__ == '__main__':
	Songloader(["Caro Emerald"])
	# caro =
	#sanitize(caro)


