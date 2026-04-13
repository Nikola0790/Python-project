create_tables_command = """
CREATE TABLE cinemas (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    address TEXT
);

CREATE TABLE Movies (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    rating INTEGER
);

CREATE TABLE Tickets (
    id SERIAL PRIMARY KEY,
    quantity INTEGER,
    price NUMERIC(10,2)
);

CREATE TABLE Payments (
    id SERIAL PRIMARY KEY,
    type VARCHAR(50),
    date DATE DEFAULT CURRENT_DATE
);
"""
