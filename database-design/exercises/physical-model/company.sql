CREATE DATABASE company;
USE company;

CREATE TABLE Employee (
    registration_number  VARCHAR(10)   NOT NULL,
    full_name            VARCHAR(100)  NOT NULL,
    gender               CHAR(1)       NOT NULL,
    birth_date           DATE          NOT NULL,
    cpf                  CHAR(11)      NOT NULL,
    rg                   VARCHAR(20)   NULL,
    marital_status       VARCHAR(20)   NOT NULL,
    CONSTRAINT pk_employee        PRIMARY KEY (registration_number),
    CONSTRAINT uq_cpf             UNIQUE (cpf),
    CONSTRAINT ck_gender          CHECK (gender IN ('M', 'F', 'O')),
    CONSTRAINT ck_marital_status  CHECK (marital_status IN ('Single', 'Married', 'Divorced', 'Widowed', 'Domestic Partnership'))
);

CREATE TABLE Parentage (
    registration_number VARCHAR(10)   NOT NULL,
    father_name         VARCHAR(100)  NOT NULL,
    mother_name         VARCHAR(100)  NOT NULL,
    CONSTRAINT pk_parentage  PRIMARY KEY (registration_number),
    CONSTRAINT fk_par_emp    FOREIGN KEY (registration_number) REFERENCES Employee(registration_number)
);

CREATE TABLE Spouse (
    registration_number VARCHAR(10)   NOT NULL,
    spouse_name         VARCHAR(100)  NOT NULL,
    CONSTRAINT pk_spouse   PRIMARY KEY (registration_number),
    CONSTRAINT fk_sps_emp  FOREIGN KEY (registration_number) REFERENCES Employee(registration_number)
);

CREATE TABLE Address (
    address_id          INT           NOT NULL,
    registration_number VARCHAR(10)   NOT NULL,
    street              VARCHAR(100)  NOT NULL,
    number              VARCHAR(10)   NOT NULL,
    complement          VARCHAR(50)   NULL,
    neighborhood        VARCHAR(60)   NOT NULL,
    city                VARCHAR(60)   NOT NULL,
    state               CHAR(2)       NOT NULL,
    zip_code            CHAR(8)       NOT NULL,
    CONSTRAINT pk_address   PRIMARY KEY (address_id),
    CONSTRAINT fk_addr_emp  FOREIGN KEY (registration_number) REFERENCES Employee(registration_number),
    CONSTRAINT ck_state     CHECK (state IN (
        'AC','AL','AM','AP','BA','CE','DF','ES',
        'GO','MA','MG','MS','MT','PA','PB','PE',
        'PI','PR','RJ','RN','RO','RR','RS','SC',
        'SE','SP','TO'
    ))
);

DROP DATABASE empresa;