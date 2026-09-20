CREATE TABLE Salesperson (
    Code       INT NOT NULL AUTO_INCREMENT COMMENT 'Unique identifier of the salesperson',
    Name       VARCHAR(100) NOT NULL COMMENT 'Salesperson name',
    Address    VARCHAR(255) COMMENT 'Salesperson address',
    Commission DECIMAL(10,2) COMMENT 'Salesperson commission',
    PRIMARY KEY (Code)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


CREATE TABLE Warehouse (
    Code    INT NOT NULL AUTO_INCREMENT COMMENT 'Unique identifier of the warehouse',
    Address VARCHAR(255) COMMENT 'Warehouse address',
    PRIMARY KEY (Code)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


CREATE TABLE Customer (
    Code               INT NOT NULL AUTO_INCREMENT COMMENT 'Unique identifier of the customer',
    Name               VARCHAR(100) NOT NULL COMMENT 'Customer name',
    Address            VARCHAR(255) COMMENT 'Customer address',
    AccumulatedRevenue DECIMAL(15,2) DEFAULT 0 COMMENT 'Customer accumulated revenue',
    CreditLimit        DECIMAL(15,2) COMMENT 'Customer credit limit',
    SalespersonCode    INT NOT NULL COMMENT 'Code of the salesperson who serves the customer',
    PRIMARY KEY (Code),
    CONSTRAINT fk_customer_salesperson
        FOREIGN KEY (SalespersonCode) REFERENCES Salesperson (Code)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


CREATE TABLE Part (
    Code          INT NOT NULL AUTO_INCREMENT COMMENT 'Unique identifier of the part',
    Description   VARCHAR(100) NOT NULL COMMENT 'Part description',
    Price         DECIMAL(10,2) NOT NULL COMMENT 'Part price',
    StockQuantity INT DEFAULT 0 COMMENT 'Quantity available in stock',
    WarehouseCode INT NOT NULL COMMENT 'Code of the warehouse where the part is stored',
    PRIMARY KEY (Code),
    CONSTRAINT fk_part_warehouse
        FOREIGN KEY (WarehouseCode) REFERENCES Warehouse (Code)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


CREATE TABLE `Order` (
    Number          INT NOT NULL AUTO_INCREMENT COMMENT 'Unique identifier of the order',
    OrderDate       DATE NOT NULL COMMENT 'Order date',
    CustomerCode    INT NOT NULL COMMENT 'Code of the customer who placed the order',
    CustomerName    VARCHAR(100) COMMENT 'Name of the customer who placed the order',
    CustomerAddress VARCHAR(255) COMMENT 'Address of the customer who placed the order',
    SalespersonCode INT NOT NULL COMMENT 'Code of the salesperson associated with the order',
    PRIMARY KEY (Number),
    CONSTRAINT fk_order_customer
        FOREIGN KEY (CustomerCode) REFERENCES Customer (Code)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,
    CONSTRAINT fk_order_salesperson
        FOREIGN KEY (SalespersonCode) REFERENCES Salesperson (Code)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


CREATE TABLE OrderItem (
    ID          INT NOT NULL AUTO_INCREMENT COMMENT 'Unique identifier of the order item',
    OrderNumber INT NOT NULL COMMENT 'Number of the order this item belongs to',
    PartCode    INT NOT NULL COMMENT 'Code of the part referenced by the item',
    Quantity    INT NOT NULL COMMENT 'Quantity of the part in the order',
    QuotedPrice DECIMAL(10,2) NOT NULL COMMENT 'Quoted price of the part in the order',
    PRIMARY KEY (ID),
    CONSTRAINT fk_orderitem_order
        FOREIGN KEY (OrderNumber) REFERENCES `Order` (Number)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT fk_orderitem_part
        FOREIGN KEY (PartCode) REFERENCES Part (Code)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


CREATE INDEX idx_customer_salesperson ON Customer (SalespersonCode);
CREATE INDEX idx_part_warehouse ON Part (WarehouseCode);
CREATE INDEX idx_order_customer ON `Order` (CustomerCode);
CREATE INDEX idx_order_salesperson ON `Order` (SalespersonCode);
CREATE INDEX idx_orderitem_order ON OrderItem (OrderNumber);
CREATE INDEX idx_orderitem_part ON OrderItem (PartCode);