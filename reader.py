import sqlite3
import requests
import psycopg2


class Reader():
	def __init__(self, db):
		self.db = db
		self.db_connect()

	def __str__(self):
		pass

	def db_connect(self):
		# Connect to an existing database
		conn = psycopg2.connect(database="musicbrainz_db",
								user="musicbrainz", password="musicbrainz",
								port="5432", host="localhost")
		print("Connection established")
		# Open a cursor to perform database operations
		cur = conn.cursor()


		# Query the database and obtain data as Python objects
		cur.execute("SELECT * FROM pg_catalog.pg_tables")
		print(cur.fetchall())
		# Make the changes to the database persistent
		#conn.commit()

		# Close communication with the database
		cur.close()
		conn.close()

#	def get_stats(self):



artists = ['The Beatles',
'Elvis Presley',
'Michael Jackson',
'Madonna',
'Elton John',
'Led Zeppelin',
'Pink Floyd']
Reader('db/mbdump/artist')