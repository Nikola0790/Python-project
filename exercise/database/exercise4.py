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


# Exercise 4
# Write SQL queries to fill each table in the database named cinemas_db 
# with at least a few entries (add them to variables in the exercise4.py file).

#   Add 3 cinemas to the table Cinemas.
#   Add 3 payments to the table Payments.

add_cinemas = "INSERT INTO cinemas (name, address) VALUES ('Tuckwood', 'Kneza Milosa 7a'), ('Roda', 'Pozeska 83'), ('MTS Dvorana', 'Decanska 14');"
add_payments = "INSERT INTO payments (type, date) VALUES ('Debit card', '2026-04-14'), ('Cash', '2026-04-14'), ('E Wallet', '2026-04-11');"