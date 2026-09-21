CREATE TABLE Cars (
    id INT PRIMARY KEY,
    model VARCHAR(50),
    year INT,
    doors INT
);

INSERT INTO Cars (id, model, year, doors) VALUES 
(1, 'BMW 320i', 2020, 4),
(2, 'Mercedes-Benz A-Class', 2021, 2),
(3, 'Audi A4', 2022, 4),
(4, 'Volkswagen Golf', 2019, 2),
(5, 'Porsche 911', 2023, 2),
(6, 'Tesla Model 3', 2021, 4),
(7, 'Jaguar XE', 2020, 4),
(8, 'Lexus IS', 2022, 4),
(9, 'Bentley Continental', 2021, 4),
(10, 'Rolls-Royce Ghost', 2020, 4);

DELETE FROM Cars
WHERE doors = 2;


