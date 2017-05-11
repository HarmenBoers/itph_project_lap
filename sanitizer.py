import musicbrainzngs
import re
import unicodedata

musicbrainzngs.set_useragent(
	"python-musicbrainzngs-example",
	"0.1",
	"https://github.com/alastair/python-musicbrainzngs/",
)

def sanitize_song_names():
	artist_dict = {}
	#Do STUFF with the song names
	artists = ['Caro Emerald']
	song_names = []
	lyric_list =[]
		#Get the first results and put in dictionary (required to get teh recording count
	for a in artists:
		artist_dict[a] = musicbrainzngs.search_recordings(artist=a, limit=25)
	for a in artists:
		print(artist_dict)
		for recording in artist_dict[a]['recording-list']:
			song_name = recording['title']
			song_name = sanitize_item(song_name)
			# a = sanitize_recording(a)
			#duplicatecheck
			print(song_name)

			song_names.append(song_name)
	print("#################")
	for s in set(song_names):
		s = strip_accents(s)
		s = re.sub('[^a-zA-Z0-9]',"", s)
		lyric_list.append(s)
		print(s)
	print(set(lyric_list))
	# for artist_DICT
	# 	add sanitized name
	# 	check if name exists

def sanitize_item(song_name):
		if '(' in song_name:
			until = song_name.index('(')
			song_name = song_name[:until]
		return song_name.lower()

def strip_accents(s):
	return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')
sanitize_song_names()