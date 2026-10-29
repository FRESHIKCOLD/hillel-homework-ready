-- 1. Імена, породи та вага всіх собак.
SELECT name, breed, weight FROM Dogs;

-- 2. Собаки, вага яких більша за 25 кг.
SELECT * FROM Dogs WHERE weight > 25;

-- 3. Власники з Києва.
SELECT name, email FROM Owners WHERE city = 'Kyiv';

-- 4. Безпородні собаки.
SELECT name, birth_year FROM Dogs WHERE breed = 'mixed';

-- 5. П'ять найдорожчих візитів.
SELECT reason, visit_date, price FROM Visits
ORDER BY price DESC, id ASC LIMIT 5;
