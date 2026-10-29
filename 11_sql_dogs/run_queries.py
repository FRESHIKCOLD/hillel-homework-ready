import sqlite3
from pathlib import Path

folder = Path(__file__).resolve().parent
with sqlite3.connect(folder / "lesson13.db") as connection:
    queries = (folder / "queries.sql").read_text(encoding="utf-8").split(";")
    for number, query in enumerate(queries, 1):
        if query.strip():
            print(f"\nЗавдання {number}")
            for row in connection.execute(query):
                print(row)
