SELECT
	artist."name",
	track."name"
FROM
	musicbrainz.musicbrainz.artist artist,
	musicbrainz.musicbrainz.track track
WHERE
	artist."id" = track.artist_credit AND
	artist."name" = 'Taylor Swift'
GROUP BY
	track."name", artist."name"