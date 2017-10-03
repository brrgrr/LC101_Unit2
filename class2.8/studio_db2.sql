-- #1
SELECT DISTINCT country FROM directors;

-- #2
SELECT first, last FROM directors WHERE country = 'France';

-- #3
SELECT MIN(date_viewed) FROM viewings;

-- #4
SELECT COUNT(m.title) FROM movies m JOIN directors d ON m.director_id = d.director_id WHERE d.country = 'USA';

-- #5
SELECT m.title FROM movies m JOIN directors d ON m.director_id = d.director_id WHERE d.first = 'Akira' and d.last = 'Kurosawa';

-- #6
SELECT COUNT(v.movie_id) FROM movies m JOIN viewings v ON m.movie_id = v.movie_id WHERE m.title = 'Talk to Me';

-- #7
SELECT MAX(date_viewed) FROM viewings;

-- #8
SELECT movie_id FROM viewings ORDER BY date_viewed DESC LIMIT 1;

-- #9
SELECT m.title FROM viewings v JOIN movies m ON m.movie_id = v.movie_id ORDER BY v.date_viewed ASC LIMIT 1;

-- #10
SELECT v.first, v.last FROM viewers v JOIN viewings vm ON v.viewer_id = vm.viewer_id ORDER BY vm.date_viewed DESC LIMIT 1;

-- #11
SELECT m.title, count(m.title) AS viewed FROM movies m JOIN viewings v ON m.movie_id = v.movie_id GROUP BY m.title ORDER BY viewed DESC;

-- #12
SELECT vr.email FROM viewers vr JOIN viewings v ON vr.viewer_id = v.viewer_id JOIN movies m ON m.movie_id = v.movie_id WHERE m.title = 'The Tango Lesson';

-- #13
SELECT DISTINCT CONCAT_WS(' ', vr.first, vr.last) as full_name, vr.email FROM viewers vr JOIN viewings v ON vr.viewer_id = v.viewer_id JOIN movies m ON m.movie_id = v.movie_id JOIN directors d ON d.director_id = m.director_id WHERE d.first = 'Akira' AND d.last = 'Kurosawa';