CREATE TABLE address (
    address_id INT AUTO_INCREMENT PRIMARY KEY,
    zip_code VARCHAR(10),
    street VARCHAR(100),
    neighborhood VARCHAR(100),
    street_number VARCHAR(10),
    city VARCHAR(100)
);

CREATE TABLE pharmacy (
    pharmacy_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    address_id INT,
    FOREIGN KEY (address_id) REFERENCES address(address_id)
);

CREATE TABLE patient (
    patient_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    tax_id CHAR(11),
    age INT,
    has_allergy BOOLEAN,
    address_id INT,
    FOREIGN KEY (address_id) REFERENCES address(address_id)
);

CREATE TABLE doctor (
    doctor_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    specialty VARCHAR(100),
    years_experience INT,
    medical_license VARCHAR(20)
);

CREATE TABLE prescription (
    prescription_id INT AUTO_INCREMENT PRIMARY KEY,
    prescription_date DATE,
    patient_id INT,
    doctor_id INT,
    FOREIGN KEY (patient_id) REFERENCES patient(patient_id),
    FOREIGN KEY (doctor_id) REFERENCES doctor(doctor_id)
);

CREATE TABLE medication (
    medication_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    commercial_name VARCHAR(100),
    formula_components TEXT,
    medication_code VARCHAR(50),
    expiration_date DATE
);

CREATE TABLE prescription_medication (
    prescription_id INT,
    medication_id INT,
    PRIMARY KEY (prescription_id, medication_id),
    FOREIGN KEY (prescription_id) REFERENCES prescription(prescription_id),
    FOREIGN KEY (medication_id) REFERENCES medication(medication_id)
);

CREATE TABLE sale (
    sale_id INT AUTO_INCREMENT PRIMARY KEY,
    sale_date DATE,
    total_price DECIMAL(10,2),
    patient_id INT,
    pharmacy_id INT,
    FOREIGN KEY (patient_id) REFERENCES patient(patient_id),
    FOREIGN KEY (pharmacy_id) REFERENCES pharmacy(pharmacy_id)
);

CREATE TABLE sale_medication (
    sale_id INT,
    medication_id INT,
    PRIMARY KEY (sale_id, medication_id),
    FOREIGN KEY (sale_id) REFERENCES sale(sale_id),
    FOREIGN KEY (medication_id) REFERENCES medication(medication_id)
);

INSERT INTO address (zip_code, street, neighborhood, street_number, city) VALUES
('SW1A1AA', 'Downing Street', 'Westminster', '10', 'London'),
('NW16XE', 'Baker Street', 'Marylebone', '221B', 'London'),
('EC1A1BB', 'St Martin Le Grand', 'City of London', '1', 'London');

INSERT INTO pharmacy (name, address_id) VALUES
('Boots Pharmacy', 1),
('LloydsPharmacy', 2),
('Superdrug Pharmacy', 3);

INSERT INTO patient (name, tax_id, age, has_allergy, address_id) VALUES
('Emily Johnson', 'AB123456C', 34, TRUE, 1),
('James Smith', 'CD987654E', 41, FALSE, 2),
('Olivia Brown', 'EF456789G', 29, TRUE, 3);

INSERT INTO doctor (name, specialty, years_experience, medical_license) VALUES
('Dr. William Thompson', 'Cardiology', 18, 'GMC-7012345'),
('Dr. Sarah Collins', 'Dermatology', 10, 'GMC-7087654'),
('Dr. Daniel Harris', 'General Practice', 22, 'GMC-7098765');

INSERT INTO prescription (prescription_date, patient_id, doctor_id) VALUES
('2025-09-10', 1, 1),
('2025-09-11', 2, 2),
('2025-09-12', 3, 3);

INSERT INTO medication (name, commercial_name, formula_components, medication_code, expiration_date) VALUES
('Paracetamol', 'Panadol', 'Paracetamol 500 mg', 'UKMED001', '2026-05-20'),
('Ibuprofen', 'Nurofen', 'Ibuprofen 400 mg', 'UKMED002', '2026-08-15'),
('Amoxicillin', 'Amoxil', 'Amoxicillin 500 mg', 'UKMED003', '2026-12-10');

INSERT INTO prescription_medication (prescription_id, medication_id) VALUES
(1, 1),
(2, 2),
(3, 3);

INSERT INTO sale (sale_date, total_price, patient_id, pharmacy_id) VALUES
('2025-09-10', 25.90, 1, 1),
('2025-09-11', 32.50, 2, 2),
('2025-09-12', 45.00, 3, 3);

INSERT INTO sale_medication (sale_id, medication_id) VALUES
(1, 1),
(2, 2)