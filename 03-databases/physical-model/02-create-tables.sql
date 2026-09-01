INSERT INTO COMPANY (name, address) VALUES 
('Global Auto Parts Inc', 'Pine Avenue, 123, New York'),
('International Logistics Group', 'Fifth Avenue, 456, London'),
('Fine Dining & Co Restaurant', 'Champs Élysées, 789, Paris'),
('Heavy Transport Solutions', 'Broadway, 202, Los Angeles'),
('Express Freight Services', 'Shibuya Street, 789, Tokyo');

INSERT INTO AGENT (ID, name) VALUES 
('98765432100', 'John Smith'),
('87654321011', 'Patricia Johnson'),
('76543210922', 'Robert Williams'),
('65432109833', 'Mary Brown'),
('54321098744', 'David Lee');

INSERT INTO PERSON (ID, name, driverLicense) VALUES 
('12345678901', 'James Anderson', '123456789'),
('23456789012', 'Sophie Martin', '987654321'),
('34567890123', 'Michael Schmidt', '234567890'),
('45678901234', 'Emma Wilson', '345678901'),
('56789012345', 'Giovanni Rossi', '456789012');

INSERT INTO VEHICLE (plateV, yearV, model, state, ID) VALUES 
('NY-1001', 2020, 'Volvo FH16', 'NY', '12345678901'),
('LN-2002', 2021, 'MAN TGX', 'LN', '23456789012'),
('PA-3003', 2022, 'Scania R450', 'PA', '34567890123'),
('LA-4004', 2023, 'Peterbilt 579', 'LA', '45678901234'),
('TK-5005', 2024, 'Isuzu Giga', 'TK', '56789012345');

INSERT INTO TRUCK (plateTruck, numberAxle, weight) VALUES  
('NY-1001', 4, 12000.50),
('LN-2002', 6, 15000.75),
('PA-3003', 8, 20000.00),
('LA-4004', 4, 18000.25),
('TK-5005', 6, 19000.50);

INSERT INTO VEHICLE (plateV, yearV, model, state, cpf) VALUES 
('NY-6006', 2020, 'Tesla Model 3', 'NY', '12345678901'),
('LN-7007', 2021, 'BMW 3 Series', 'LN', '23456789012'),
('PA-8008', 2022, 'Audi A4', 'PA', '34567890123'),
('LA-9009', 2023, 'Mercedes-Benz C-Class', 'LA', '45678901234'),
('TK-1010', 2024, 'Lexus IS', 'TK', '56789012345');

INSERT INTO CAR (plateCar, numDoors, descC) VALUES 
('NY-6006', 4, 'Tesla Model 3 - Electric'),
('LN-7007', 2, 'BMW 3 Series - Premium'),
('PA-8008', 4, 'Audi A4 - Luxury'),
('LA-9009', 4, 'Mercedes-Benz C-Class - Luxury'),
('TK-1010', 4, 'Lexus IS - Premium');

INSERT INTO PHONES (ID, number) VALUES 
('12345678901', '11987654321'), 
('23456789012', '21987654321'), 
('34567890123', '31987654321'), 
('45678901234', '41987654321'), 
('56789012345', '51987654321');

INSERT INTO LOCATION (speedAllowed, street, position) VALUES 
(65, 'Park Avenue, New York', 'Manhattan'),
(80, 'Oxford Street, London', 'Westminster'),
(50, 'Rue de Rivoli, Paris', '1st Arrondissement'),
(60, 'Sunset Boulevard, Los Angeles', 'Hollywood'),
(55, 'Ginza Street, Tokyo', 'Chuo Ward');


INSERT INTO INFRACTIONTYPE (idTypeInfra, type) VALUES 
(1, 'Speeding'), 
(2, 'Disrespect of Traffic Signs'), 
(3, 'Cell Phone Use'), 
(4, 'Driving Without Seatbelt');

INSERT INTO TICKET (dateDue) VALUES 
('2024-11-15'),
('2024-11-20'),
('2024-11-25'),
('2024-12-01'),
('2024-12-05');

INSERT INTO INFRACTION (speed, dateInfra, idTypeInfra, plateV, ID, idLocation, numTicket) VALUES 
(75.50, '2024-10-25', 1, 'NY-6006', '98765432100', 1, 1),
(95.00, '2024-10-26', 2, 'LN-7007', '87654321011', 2, 2),
(85.00, '2024-10-27', 3, 'PA-8008', '76543210922', 3, 3),
(70.00, '2024-10-28', 4, 'LA-9009', '65432109833', 4, 4),
(88.00, '2024-10-29', 1, 'TK-1010', '54321098744', 5, 5);

SELECT * FROM COMPANY;
SELECT * FROM AGENT;
SELECT * FROM PERSON;
SELECT * FROM VEHICLE;
SELECT * FROM TRUCK;
SELECT * FROM CAR;
SELECT * FROM PHONES;
SELECT * FROM LOCATION;
SELECT * FROM INFRACTION;
SELECT * FROM TICKET;