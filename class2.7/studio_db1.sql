-- https://www.db-fiddle.com/f/febFK4ZnbMz8kZEowgQ13f/4
/* Schema */
create table movies (
	movie_id INTEGER AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100),
    year INTEGER,
    director_id INTEGER
);

create table directors (
	director_id INTEGER AUTO_INCREMENT PRIMARY KEY,
  	name VARCHAR(100),
  	country VARCHAR(50)
);

INSERT INTO directors(name, country) values
('James Cameron', 'USA'),
('Kathryn Bigelo', 'USA'),
('Jean-Pierre Jeunet', 'France');


INSERT INTO movies(title, year, director_id) values
('Titanic', 1997, 1),
('True Lies', 1994, 1),
( 'Terminator', 1984, 1),
( 'Alien', 1986, 1),
( 'Point Break', 1991, 2),
( 'Strange Days', 1995, 2),
( 'The Hurt Locker', 2008, 2),
('Amelie', 2001, 3);

/* Query */
-- #1
select title from movies;

-- #2
select title from movies order by year desc;

/* #3
insert into directors (name, country) values ('Jean-Pierre Jeunet', 'France');
*/
-- #4
select director_id from directors  where name = 'Jean-Pierre Jeunet';
/* #5
insert into movies (title, year, director_id) values ('Amelie', 2001, 3);
*/
-- #6
select * from directors order by country;

-- #7
select m.title, d.country from movies m join directors d on m.director_id = d.director_id where m.title = 'Amelie';

-- #8
select m.title, SUBSTRING_INDEX(d.name, ' ', 1) AS first, SUBSTRING_INDEX(d.name, ' ', -1) AS last from movies m join directors d on m.director_id = d.director_id order by last;

