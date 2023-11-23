SELECT album_name, release_year FROM albums
WHERE release_year=2018;
SELECT song_name, duration FROM songs 
WHERE duration IN (SELECT MAX(duration) FROM songs);
SELECT song_name FROM songs
WHERE duration>='00:03:30';
SELECT collection_name FROM collection
WHERE release_year BETWEEN 2018 AND 2020;
SELECT * FROM musicians
WHERE nickname NOT LIKE '% %';
SELECT song_name FROM songs
WHERE song_name LIKE '%Мой%';