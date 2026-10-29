CREATE TABLE books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    publication_year INTEGER NOT NULL,
    price REAL NOT NULL CHECK (price >= 0)
);

INSERT INTO books (title, author, publication_year, price) VALUES
('Кобзар', 'Тарас Шевченко', 1840, 350.00),
('Лісова пісня', 'Леся Українка', 1911, 280.00),
('Захар Беркут', 'Іван Франко', 1883, 300.00);

UPDATE books SET price = 375.00 WHERE id = 1;
DELETE FROM books WHERE id = 3;
SELECT * FROM books;
