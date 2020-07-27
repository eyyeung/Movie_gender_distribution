from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

from werkzeug.exceptions import abort

from movieinfo.db import get_db


bp = Blueprint('movies', __name__)

@bp.route("/")
def index():
    return render_template("index.html")

@bp.route("/movies")
def get_movies():
    db = get_db()
    movies = db.execute(
        'SELECT * FROM movies LIMIT 50'
    ).fetchall()
    return render_template('movies.html', movies=movies)

@bp.route("/<int:id>", methods=['GET','POST'])
def get_movie_detail(id):
    movie = get_db().execute(
        'SELECT m.id, m.primaryTitle as title, m.startYear, m.runtimeMinutes, m.averageRating, m.numVotes, m.bechdel,COUNT(p.nconst) as numPeople FROM movies m INNER JOIN cast c ON c.tconst = m.tconst INNER JOIN people p ON p.nconst = c.nconst WHERE m.id=?',(id,)
    ).fetchone()

    return render_template('movie.html', movie=movie)

@bp.route("/cast")
def get_cast():
    db = get_db()
    cast = db.execute(
        'SELECT m.primaryTitle as title, p.name as name, c.category ,c.ordering FROM cast c INNER JOIN movies m ON c.tconst=m.tconst INNER JOIN people p ON p.nconst = c.nconst LIMIT 50'
    ).fetchall()
    return render_template('cast.html', cast=cast)

@bp.route("/people")
def get_people():
    db = get_db()
    people = db.execute(
        'SELECT * FROM people LIMIT 50'
    ).fetchall()
    return render_template('people.html', people=people)
