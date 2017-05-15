import csv
import musicbrainzngs
musicbrainzngs.set_useragent(
	"python-musicbrainzngs-example",
	"0.1",
	"https://github.com/alastair/python-musicbrainzngs/",
)

song_names = []
artists = []

with open('top40_songs_tester.csv', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile, delimiter='\t')
    for row in reader:
        work = musicbrainzngs.search_works(recording=row['title'], limit=25)
        print(work)
