from __future__ import print_function
from __future__ import unicode_literals
import musicbrainzngs
import sys

print(sys.getdefaultencoding())


musicbrainzngs.set_useragent(
	"python-musicbrainzngs-example",
	"0.1",
	"https://github.com/alastair/python-musicbrainzngs/",
)

if __name__ == '__main__':
	# args = sys.argv[1:]
	# Keyword arguments to the "search_*" functions limit keywords to
	# specific fields. The "limit" keyword argument is special (like as
	# "offset", not shown here) and specifies the number of results to
	# return.
	artists = ['The Beatles','Elvis Presley','Michael Jackson','Madonna','Elton John','Led Zeppelin', 'Pink Floyd', 'Bob Dylan']
	result = {}
	for a in artists:
		result[a] = musicbrainzngs.search_recordings(artist=a, limit=10)
	print(result)
	for a in artists:
		print(a + ": " + str(result[a]['recording-list']))
	#
	# print([k.encode('UTF8') for k in result.keys()])
	# print([s.encode('UTF8') for s in [k for k in result.values()]])

	# print(result)
	# On success, result is a dictionary with a single key:
	# "release-list", which is a list of dictionaries.
