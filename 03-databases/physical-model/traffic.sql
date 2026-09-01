CREATE TABLE Agent (
    agentCpf  VARCHAR(11)  PRIMARY KEY,
    agentName VARCHAR(100) NOT NULL
);

CREATE TABLE Person (
    cpf           VARCHAR(11)  PRIMARY KEY,
    name          VARCHAR(100) NOT NULL,
    driverLicense VARCHAR(20)  NOT NULL
);

CREATE TABLE Vehicle (
    licensePlate VARCHAR(10)  PRIMARY KEY,
    year         YEAR         NOT NULL,
    model        VARCHAR(100) NOT NULL,
    state        CHAR(2)      NOT NULL,
    cpf          VARCHAR(11),
    FOREIGN KEY (cpf) REFERENCES Person(cpf)
);

CREATE TABLE Truck (
    truckPlate VARCHAR(10)    PRIMARY KEY,
    axleCount  INT            NOT NULL,
    weight     DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (truckPlate) REFERENCES Vehicle(licensePlate)
);

CREATE TABLE Car (
    carPlate    VARCHAR(10)  PRIMARY KEY,
    doorCount   INT          NOT NULL,
    description VARCHAR(255) NOT NULL,
    FOREIGN KEY (carPlate) REFERENCES Vehicle(licensePlate)
);

CREATE TABLE Phones (
    cpf    VARCHAR(11) NOT NULL,
    number VARCHAR(15) NOT NULL,
    PRIMARY KEY (cpf, number),
    FOREIGN KEY (cpf) REFERENCES Person(cpf)
);

CREATE TABLE ViolationType (
    violationTypeId INT            PRIMARY KEY AUTO_INCREMENT,
    severityLevel   VARCHAR(50)    NOT NULL,
    fine            DECIMAL(10, 2) NOT NULL,
    description     VARCHAR(255)   NOT NULL
);

CREATE TABLE Ticket (
    ticketNumber INT  PRIMARY KEY AUTO_INCREMENT,
    dueDate      DATE NOT NULL
);

CREATE TABLE Location (
    locationId INT          PRIMARY KEY AUTO_INCREMENT,
    speedLimit INT          NOT NULL,
    street     VARCHAR(255) NOT NULL,
    position   POINT        NOT NULL
);

CREATE TABLE Violation (
    violationId     INT           PRIMARY KEY AUTO_INCREMENT,
    speed           DECIMAL(5, 2) NOT NULL,
    violationDate   DATE          NOT NULL,
    violationTypeId INT,
    licensePlate    VARCHAR(10),
    agentCpf        VARCHAR(11),
    locationId      INT,
    ticketNumber    INT,
    FOREIGN KEY (violationTypeId) REFERENCES ViolationType(violationTypeId),
    FOREIGN KEY (licensePlate)    REFERENCES Vehicle(licensePlate),
    FOREIGN KEY (agentCpf)        REFERENCES Agent(agentCpf),
    FOREIGN KEY (locationId)      REFERENCES Location(locationId),
    FOREIGN KEY (ticketNumber)    REFERENCES Ticket(ticketNumber)
);