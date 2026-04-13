# Triple-quoted string (""" ... """) in the Python code. 
# This allows you to write multiple lines of SQL inside one variable, 
# which makes it much easier to read than one giant single line.

create_tables_command = """
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    description TEXT,
    price NUMERIC(5,2)
);

CREATE TABLE Orders (
    id SERIAL PRIMARY KEY,
    description TEXT
);

CREATE TABLE Customers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    surname VARCHAR(255)
);
"""
