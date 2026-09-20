CREATE TABLE Agent (
    cpfA VARCHAR(11) PRIMARY KEY,
    nameA VARCHAR(100) NOT NULL
);

CREATE TABLE Person (
    cpf VARCHAR(11) PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    driverLicense VARCHAR(20) NOT NULL
);

CREATE TABLE Vehicle (
    plateV VARCHAR(10) PRIMARY KEY,
    yearV YEAR NOT NULL,
    model VARCHAR(100) NOT NULL,
    state CHAR(2) NOT NULL,
    cpf VARCHAR(11),
    FOREIGN KEY (cpf) REFERENCES Person(cpf)
);

CREATE TABLE Truck (
    plateTruck VARCHAR(10) PRIMARY KEY,
    numberAxle INT NOT NULL,
    weight DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (plateTruck) REFERENCES Vehicle(plateV)
);

CREATE TABLE Car (
    plateCar VARCHAR(10) PRIMARY KEY,
    numDoors INT NOT NULL,
    descC VARCHAR(255) NOT NULL,
    FOREIGN KEY (plateCar) REFERENCES Vehicle(plateV)
);

CREATE TABLE Phones (
    cpf VARCHAR(11),
    number VARCHAR(15) NOT NULL,
    PRIMARY KEY (cpf, number),
    FOREIGN KEY (cpf) REFERENCES Person(cpf)
);

CREATE TABLE InfractionType (
    idTypeInfra INT PRIMARY KEY AUTO_INCREMENT,
    severityLevel VARCHAR(50) NOT NULL,
    value DECIMAL(10, 2) NOT NULL,
    descI VARCHAR(255) NOT NULL
);

CREATE TABLE Ticket (
    numTicket INT PRIMARY KEY AUTO_INCREMENT,
    dateDue DATE NOT NULL
);

CREATE TABLE Location (
    idLocation INT PRIMARY KEY AUTO_INCREMENT,
    speedAllowed INT NOT NULL,
    street VARCHAR(255) NOT NULL,
    position POINT NOT NULL
);

CREATE TABLE Infraction (
    idInfraction INT PRIMARY KEY AUTO_INCREMENT,
    speed DECIMAL(5, 2) NOT NULL,
    dateInfra DATE NOT NULL,
    idTypeInfra INT,
    plateV VARCHAR(10),
    cpfA VARCHAR(11),
    idLocation INT,
    numTicket INT,
    FOREIGN KEY (idTypeInfra) REFERENCES InfractionType(idTypeInfra),
    FOREIGN KEY (plateV) REFERENCES Vehicle(plateV),
    FOREIGN KEY (cpfA) REFERENCES Agent(cpfA),
    FOREIGN KEY (idLocation) REFERENCES Location(idLocation),
    FOREIGN KEY (numTicket) REFERENCES Ticket(numTicket)
);
