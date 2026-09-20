CREATE TABLE Seller (
    Code        INT             PRIMARY KEY,
    Name        VARCHAR(100)    NOT NULL,
    Address     VARCHAR(255)    NOT NULL,
    Commission  DECIMAL(10, 2)  NOT NULL
);

CREATE TABLE Customer (
    Code                INT             PRIMARY KEY,
    Name                VARCHAR(100)    NOT NULL,
    Address             VARCHAR(255)    NOT NULL,
    AccumulatedBilling  DECIMAL(15, 2)  NOT NULL,
    CreditLimit         DECIMAL(15, 2)  NOT NULL,
    SellerCode          INT,
    FOREIGN KEY (SellerCode) REFERENCES Seller(Code)
);

CREATE TABLE Warehouse (
    Code     INT          PRIMARY KEY,
    Address  VARCHAR(255) NOT NULL
);

CREATE TABLE Part (
    Code         INT             PRIMARY KEY,
    Description  VARCHAR(100)    NOT NULL,
    Price        DECIMAL(10, 2)  NOT NULL,
    StockQty     INT             NOT NULL,
    WarehouseCode INT,
    FOREIGN KEY (WarehouseCode) REFERENCES Warehouse(Code)
);

CREATE TABLE Order_ (
    OrderNumber      INT          PRIMARY KEY,
    OrderDate        DATE         NOT NULL,
    CustomerCode     INT,
    CustomerName     VARCHAR(100) NOT NULL,
    CustomerAddress  VARCHAR(255) NOT NULL,
    SellerCode       INT,
    FOREIGN KEY (CustomerCode) REFERENCES Customer(Code),
    FOREIGN KEY (SellerCode)   REFERENCES Seller(Code)
);

CREATE TABLE OrderItem (
    ID           INT             PRIMARY KEY,
    OrderNumber  INT,
    PartCode     INT,
    Quantity     INT             NOT NULL,
    QuotedPrice  DECIMAL(10, 2)  NOT NULL,
    FOREIGN KEY (OrderNumber) REFERENCES Order_(OrderNumber),
    FOREIGN KEY (PartCode)    REFERENCES Part(Code)
);