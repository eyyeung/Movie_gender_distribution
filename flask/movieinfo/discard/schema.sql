DROP TABLE IF EXISTS movies;
DROP TABLE IF EXISTS people;
DROP TABLE IF EXISTS movie_genres;
DROP TABLE IF EXISTS genres;

CREATE TABLE movie (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT UNIQUE NOT NULL,
    startYear INTEGER NOT NULL,
    runTime INTEGER,
    avgRating INTEGER,
    numVote INTEGER,
    bechdelScore INTEGER
);

CREATE TABLE people (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    movie_id INTEGER NOT NULL,
    gender TEXT,
    birthYear INTEGER,
    job TEXT NOT NULL,
    FOREIGN KEY (movie_id) REFERENCES movie (id)
);

CREATE TABLE genres (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    genre TEXT
);

CREATE TABLE movie_genres (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    movie_id INTEGER NOT NULL,
    genre_id INTEGER NOT NULL,
    FOREIGN KEY (movie_id) REFERENCES movie (id),
    FOREIGN KEY (genre_id) REFERENCES genres (id)
);
