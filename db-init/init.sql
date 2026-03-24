CREATE TABLE Vendors (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    contact VARCHAR(255),
    rating NUMERIC(3, 2)
);

CREATE TABLE Products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    sku VARCHAR(100) UNIQUE NOT NULL,
    unit_price NUMERIC(10, 2) NOT NULL,
    stock_level INT NOT NULL
);

CREATE TABLE PurchaseOrders (
    id SERIAL PRIMARY KEY,
    reference_no VARCHAR(100) UNIQUE NOT NULL,
    vendor_id INT REFERENCES Vendors(id),
    total_amount NUMERIC(10, 2) DEFAULT 0,
    status VARCHAR(50) DEFAULT 'Pending'
);

CREATE TABLE PurchaseOrderItems (
    id SERIAL PRIMARY KEY,
    po_id INT REFERENCES PurchaseOrders(id) ON DELETE CASCADE,
    product_id INT REFERENCES Products(id),
    quantity INT NOT NULL,
    unit_price NUMERIC(10, 2) NOT NULL
);

-- Insert dummy data for Vendors (used by vendor-service or simply direct query)
INSERT INTO Vendors (name, contact, rating) VALUES ('Tech Supplies Inc', 'contact@techsupplies.com', 4.5);
INSERT INTO Vendors (name, contact, rating) VALUES ('Office World', 'sales@officeworld.com', 4.2);

-- Insert dummy data for Products
INSERT INTO Products (name, sku, unit_price, stock_level) VALUES ('Wireless Mouse', 'WM-001', 25.00, 100);
INSERT INTO Products (name, sku, unit_price, stock_level) VALUES ('Mechanical Keyboard', 'MK-102', 80.00, 50);
INSERT INTO Products (name, sku, unit_price, stock_level) VALUES ('27-inch Monitor', 'MON-27', 250.00, 30);
