from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3
from typing import List

app = FastAPI()

def get_db():
    conn = sqlite3.connect("movies.db")
    conn.row_factory = sqlite3.Row
    return conn

class Movie(BaseModel):
    id: int = None
    title: str
    director: str
    year: int

@app.on_event("startup")
def startup():
    conn = get_db()
    conn.execute("""
    CREATE TABLE IF NOT EXISTS movies (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        director TEXT NOT NULL,
        year INTEGER NOT NULL
    )
    """)
    conn.commit()
    conn.close()

@app.get("/movies", response_model=List[Movie])
def list_movies():
    conn = get_db()
    cursor = conn.execute("SELECT * FROM movies")
    movies = [Movie(**dict(row)) for row in cursor.fetchall()]
    conn.close()
    return movies

@app.post("/movies", response_model=Movie)
def create_movie(movie: Movie):
    conn = get_db()
    cursor = conn.execute(
        "INSERT INTO movies (title, director, year) VALUES (?, ?, ?)",
        (movie.title, movie.director, movie.year)
    )
    conn.commit()
    movie.id = cursor.lastrowid
    conn.close()
    return movie
