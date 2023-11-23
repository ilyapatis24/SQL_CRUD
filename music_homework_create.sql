CREATE TABLE IF NOT EXISTS music_ganre(
music_ganre_id SERIAL PRIMARY KEY,
ganre_name VARCHAR(30) NOT NULL
);
CREATE TABLE IF NOT EXISTS musicians(
musician_id SERIAL PRIMARY KEY,
nickname VARCHAR(30)
);
CREATE TABLE IF NOT EXISTS ganremusicians(
music_ganre_id INTEGER REFERENCES music_ganre(music_ganre_id),
musician_id INTEGER REFERENCES musicians(musician_id),
CONSTRAINT pk PRIMARY KEY (music_ganre_id, musician_id )
);
CREATE TABLE IF NOT EXISTS albums(
album_id SERIAL PRIMARY KEY,
album_name VARCHAR(40) NOT NULL,
release_year INTEGER
);
CREATE TABLE IF NOT EXISTS albumsmusicians(
musician_id INTEGER REFERENCES musicians(musician_id),
album_id INTEGER REFERENCES albums(album_id),
CONSTRAINT pk1 PRIMARY KEY (musician_id, album_id )
);
CREATE TABLE IF NOT EXISTS collection(
collection_id SERIAL PRIMARY KEY,
collection_name VARCHAR(30) NOT NULL,
release_year INTEGER
);
CREATE TABLE IF NOT EXISTS collection(
collection_id SERIAL PRIMARY KEY,
collection_name VARCHAR(30) NOT NULL,
release_year INTEGER
);
CREATE TABLE IF NOT EXISTS songs(
song_id SERIAL PRIMARY KEY,
song_name  VARCHAR(30) NOT NULL,
album_id INTEGER REFERENCES albums(album_id),
duration TIME
);
CREATE TABLE IF NOT EXISTS songscollection(
collection_id INTEGER REFERENCES collection(collection_id),
song_id INTEGER REFERENCES songs(song_id),
CONSTRAINT pk2 PRIMARY KEY (collection_id, song_id)
);



