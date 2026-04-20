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

# Write queries that:
#   display all products from the database exercises_db,
#   display all orders from database exercises_db,
#   display all customers from database exercises_db.
# Write the queries in the appropriate variables in the exercise2.py file.

# Retrieve all data from a table.
display_all_products = 'SELECT * FROM products;'
display_all_orders = 'SELECT * FROM orders;'
display_all_customers = 'SELECT * FROM customers;'

# Add to the Cinemas table a column that stores the number of seats (integer). Write the query in the file exercise2.py.
add_column = "ALTER TABLE cinemas ADD number_of_seats INTEGER;"

# Exercise 2
# Create a table named Comments that will allow comments on videos. 
# The table should contain a content field that will accept arbitrarily long text. 
# Link it to the Movies table with a one-to-many relationship (a movie can have multiple comments).
# Add some comments.

#Step 1
create_table_comments = 'CREATE TABLE comments (comment_id SERIAL NOT NULL, movie_id int NOT NULL, contnet TEXT, PRIMARY KEY(comment_id), FOREIGN KEY(movie_id) REFERENCES movies(id));'
#Step 2
add_comments = "INSERT INTO comments (movie_id, contnet) VALUES (2, 'Content11111'),(2, 'Content2'),(2, 'comment111'),(4, 'Comment222');"
#Step 3
join_tables_retrive_data = "SELECT * FROM movies JOIN comments ON movies.id=comments.movie_id;"