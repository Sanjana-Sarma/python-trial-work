import xml.etree.ElementTree as ET
import sqlite3

conn = sqlite3.connect('trackdb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Artist')
cur.execute('DROP TABLE IF EXISTS Genre')
cur.execute('DROP TABLE IF EXISTS Album')
cur.execute('DROP TABLE IF EXISTS Track')
cur.execute('CREATE TABLE Artist(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,name TEXT UNIQUE)')
cur.execute('CREATE TABLE Genre(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,name TEXT UNIQUE)')
cur.execute('CREATE TABLE Album(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,artist_id INTEGER,title TEXT UNIQUE)')
cur.execute('CREATE TABLE Track(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,title TEXT UNIQUE,album_id INTEGER,genre_id INTEGER,len INTEGER,rating INTEGER,count,INTEGER)')

fname = 'C:/Users/angel/OneDrive/Desktop/TEXTBOOKS/COMPUTER PROGRAMMING/PYTHON/python_work/Library.xml'
def lookup(d, key):
    found = False
    for child in d:
        if found : return child.text
        if child.tag == 'key' and child.text == key :
            found = True
    return None

stuff = ET.parse(fname)
allin = stuff.findall('dict/dict/dict')
print('Dict count:', len(allin))
for entry in allin:
	if ( lookup(entry, 'Track ID') is None ):
		continue
	name=lookup(entry,'Name')
	artist=lookup(entry,'Artist')
	album=lookup(entry,'Album')
	genre=lookup(entry,'Genre')
	count=lookup(entry,'Play Count')
	rating=lookup(entry,'Rating')
	length=lookup(entry,'Total Time')

	if name is None or artist is None or album is None or genre is None:
		continue
	print(name, artist, album, genre, count, rating, length)
	cur.execute('INSERT OR IGNORE INTO Artist(name) VALUES(?)',(artist,))
	cur.execute('SELECT id FROM Artist WHERE name=?',(artist,))
	artist_id=cur.fetchone()[0]
	cur.execute('INSERT OR IGNORE INTO Genre(name) VALUES(?)',(genre,))
	cur.execute('SELECT id FROM Genre WHERE name=?',(genre,))
	genre_id=cur.fetchone()[0]
	cur.execute('INSERT OR IGNORE INTO Album(title,artist_id) VALUES(?,?)',(album,artist_id))
	cur.execute('SELECT id FROM Album WHERE title=?',(album,))
	album_id=cur.fetchone()[0]
	cur.execute('INSERT OR IGNORE INTO Track(title,album_id,genre_id,len,rating,count) VALUES(?,?,?,?,?,?)',(name,album_id,genre_id,length,rating,count))
conn.commit()
cur.execute('SELECT Track.title, Artist.name, Album.title, Genre.name FROM Track JOIN Genre JOIN Album JOIN Artist ON Track.genre_id = Genre.ID and Track.album_id = Album.id AND Album.artist_id = Artist.id ORDER BY Artist.name LIMIT 3')
cur.close()