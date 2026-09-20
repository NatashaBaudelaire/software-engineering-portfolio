SET SQL_SAFE_UPDATES = 0;

INSERT INTO Agent (agentCpf, agentName) VALUES 
('98765432100', 'Agent 1'),
('87654321011', 'Agent 2'),
('76543210922', 'Agent 3'),
('65432109833', 'Agent 4'),
('54321098744', 'Agent 5');

INSERT INTO Person (cpf, name, driverLicense) VALUES 
('12345678901', 'Lucas Thompson',   '123456789'),
('23456789012', 'Mariana Bennett',  '987654321'),
('34567890123', 'Charles Edwards',  '234567890'),
('45678901234', 'Fernanda Collins', '345678901'),
('56789012345', 'Robert Mitchell',  '456789012');

INSERT INTO Vehicle (licensePlate, year, model, state, cpf) VALUES 
('DEF1G23', 2020, 'Truck A', 'TX', '12345678901'),
('UVW4X56', 2021, 'Truck B', 'CA', '23456789012'),
('GHI7J89', 2022, 'Truck C', 'FL', '34567890123'),
('RST1U23', 2023, 'Truck D', 'NY', '45678901234'),
('JKL4M56', 2024, 'Truck E', 'GA', '56789012345'),
('ABC1D23', 2020, 'Car A',   'TX', '12345678901'),
('XYZ4W56', 2021, 'Car B',   'CA', '23456789012'),
('LMN7O89', 2022, 'Car C',   'FL', '34567890123'),
('OPQ1R23', 2023, 'Car D',   'NY', '45678901234'),
('STU4V56', 2024, 'Car E',   'GA', '56789012345');

INSERT INTO Truck (truckPlate, axleCount, weight) VALUES  
('DEF1G23', 4, 12000.50),
('UVW4X56', 6, 15000.75),
('GHI7J89', 8, 20000.00),
('RST1U23', 4, 18000.25),
('JKL4M56', 6, 19000.50);

INSERT INTO Car (carPlate, doorCount, description) VALUES 
('ABC1D23', 4, 'Mercedes-Benz A-Class'),
('XYZ4W56', 2, 'Ford Fiesta'),
('LMN7O89', 4, 'Audi A3'),
('OPQ1R23', 2, 'Chevrolet Spark'),
('STU4V56', 4, 'BMW 3 Series');

INSERT INTO Phones (cpf, number) VALUES 
('12345678901', '14695558721'),
('23456789012', '21398554632'),
('34567890123', '31256557843'),
('45678901234', '41987556954'),
('56789012345', '51874555065');

INSERT INTO ViolationType (severityLevel, fine, description) VALUES 
('Severe',   150.00, 'Speeding'),
('Moderate', 100.00, 'Disregarding Traffic Signs'),
('Moderate', 125.00, 'Cell Phone Use'),
('Minor',     50.00, 'Driving Without Seatbelt');

INSERT INTO Ticket (dueDate) VALUES 
('2024-11-15'),
('2024-11-20'),
('2024-11-25'),
('2024-12-01'),
('2024-12-05');

INSERT INTO Location (speedLimit, street, position) VALUES 
(60, 'Palm Street',    ST_GeomFromText('POINT(30 -97)')),
(80, 'Liberty Avenue', ST_GeomFromText('POINT(34 -118)')),
(40, 'Coffee Square',  ST_GeomFromText('POINT(25 -80)')),
(50, 'Central Avenue', ST_GeomFromText('POINT(40 -74)')),
(30, 'Peace Square',   ST_GeomFromText('POINT(33 -84)'));

INSERT INTO Violation (speed, violationDate, violationTypeId, licensePlate, agentCpf, locationId, ticketNumber) VALUES 
(70.50, '2024-10-25', 1, 'ABC1D23', '98765432100', 1, 1),
(90.00, '2024-10-26', 2, 'XYZ4W56', '87654321011', 2, 2),
(80.00, '2024-10-27', 3, 'LMN7O89', '76543210922', 3, 3),
(75.00, '2024-10-28', 4, 'OPQ1R23', '65432109833', 4, 4),
(85.00, '2024-10-29', 1, 'STU4V56', '54321098744', 5, 5);

SET SQL_SAFE_UPDATES = 1;

SELECT * FROM Agent;
SELECT * FROM Person;
SELECT * FROM Vehicle;
SELECT * FROM Truck;
SELECT * FROM Car;
SELECT * FROM Phones;
SELECT * FROM ViolationType;
SELECT * FROM Ticket;
SELECT * FROM Location;
SELECT * FROM Violation;