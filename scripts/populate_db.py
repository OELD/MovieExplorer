import sqlite3

movies = [
    ("The Matrix", "Lana & Lilly Wachowski", 1999),
    ("Inception", "Christopher Nolan", 2010),
    ("Parasite", "Bong Joon-ho", 2019),
    ("Spirited Away", "Hayao Miyazaki", 2001)
]

conn = sqlite3.connect("movies.db")
cursor = conn.cursor()
cursor.executemany(
    "INSERT INTO movies (title, director, year) VALUES (?, ?, ?)",
    movies
)
conn.commit()
conn.close()
print("✅ Seeded database with sample movies!")
