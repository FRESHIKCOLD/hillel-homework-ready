import csv
import sqlite3
from pathlib import Path


class CardCollection:
    """Колекція карток зі збереженням у SQLite."""

    def __init__(self, database):
        self.connection = sqlite3.connect(database)
        self.connection.row_factory = sqlite3.Row
        self.connection.execute("""
            CREATE TABLE IF NOT EXISTS cards (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL CHECK (length(trim(name)) > 0),
                game TEXT NOT NULL CHECK (length(trim(game)) > 0),
                quantity INTEGER NOT NULL CHECK (quantity >= 0),
                notes TEXT NOT NULL DEFAULT ''
            )
        """)
        self.connection.commit()

    @staticmethod
    def validate_quantity(quantity):
        if type(quantity) is not int or quantity < 0:
            raise ValueError("Кількість має бути невід'ємним цілим числом")

    def add(self, name, game, quantity=1, notes=""):
        self.validate_quantity(quantity)
        if not name.strip() or not game.strip():
            raise ValueError("Назва картки та гри не можуть бути порожніми")
        with self.connection:
            cursor = self.connection.execute(
                "INSERT INTO cards (name, game, quantity, notes) VALUES (?, ?, ?, ?)",
                (name.strip(), game.strip(), quantity, notes.strip()),
            )
        return cursor.lastrowid

    def list_cards(self, search=""):
        # instr шукає буквальний текст: % та _ не стають SQL-шаблонами.
        return self.connection.execute(
            "SELECT * FROM cards WHERE instr(lower(name), lower(?)) > 0 ORDER BY name, id",
            (search,),
        ).fetchall()

    def update_quantity(self, card_id, quantity):
        self.validate_quantity(quantity)
        with self.connection:
            cursor = self.connection.execute(
                "UPDATE cards SET quantity = ? WHERE id = ?", (quantity, card_id)
            )
            if cursor.rowcount == 0:
                raise ValueError("Картку з таким ID не знайдено")

    def delete(self, card_id):
        with self.connection:
            cursor = self.connection.execute("DELETE FROM cards WHERE id = ?", (card_id,))
            if cursor.rowcount == 0:
                raise ValueError("Картку з таким ID не знайдено")

    def statistics(self):
        row = self.connection.execute(
            "SELECT COUNT(*) AS entries, COALESCE(SUM(quantity), 0) AS total FROM cards"
        ).fetchone()
        return dict(row)

    def export_csv(self, path):
        with Path(path).open("w", newline="", encoding="utf-8-sig") as file:
            writer = csv.DictWriter(file, fieldnames=["id", "name", "game", "quantity", "notes"])
            writer.writeheader()
            writer.writerows(dict(card) for card in self.list_cards())

    def close(self):
        self.connection.close()
