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

# Exercise 3
# Create a payment table. It should have the same data as in the exercises from the previous day, 
# but it should be related to the Ticket table by a one-to-one relationship (this will affect the id column). 
# The relation between ticket and payment is as follows: the ticket has 1 or 0 payments (it is then unpaid) – payment must be assigned to a ticket.

#Step 1 "Add FOREIGN KEY to payments table"
update_fk_payments_table = "ALTER TABLE payments ADD CONSTRAINT fk_payments_tickets FOREIGN KEY(id) REFERENCES tickets(id) ON DELETE CASCADE;"
#Step 2 "Join ticket and payments"
"SELECT * FROM tickets JOIN payments ON tickets.id = payments.id;"

# Exercise 2
# Join tables Cinemas and Movies through a many-to-many relationship 
# (a movie can be screened in many cinemas, a cinema can screen many movies).
# Additionally, name the created table Screening. In addition to the fields that refer to the tables Cinemas and Movies, 
# it should have a datetime field of the timestamp type.
# Add several screenings.

# Step 1
create_join_table_screening = "CREATE TABLE screening(id serial NOT NULL, datetime TIMESTAMP, cinema_id int NOT NULL, movie_id int NOT NULL, PRIMARY KEY(id), FOREIGN KEY(cinema_id) REFERENCES cinemas(id), FOREIGN KEY(movie_id) REFERENCES movies(id));"
# Step 2
add_data_to_join_table = "INSERT INTO screening(datetime, cinema_id, movie_id) VALUES('2026-04-24 14:30', 1, 1),('2026-04-24 17:30', 1, 3), ('2026-04-24 20:00', 2, 1),('2026-04-24 20:00', 3, 1), ('2026-04-24 17:00', 3, 3), ('2026-04-24 20:00', 2, 4);"
# Step 3
show_many_to_many_relationship = "SELECT * FROM cinemas JOIN screening ON cinemas.id = screening.cinema_id JOIN movies ON movies.id = screening.movie_id;"

#  id |      name       |     address     | number_of_seats | id |      datetime       | cinema_id | movie_id | id |    name    |                                                                                              description                                                                                              | rating
# ----+-----------------+-----------------+-----------------+----+---------------------+-----------+----------+----+------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------
#   1 | TUCKWOOD CINEMA | Kneza Milosa 7a |                 |  1 | 2026-04-24 14:30:00 |         1 |        1 |  1 | Terminator | Movie description...                                                                                                                                                                                  |      7
#   1 | TUCKWOOD CINEMA | Kneza Milosa 7a |                 |  2 | 2026-04-24 17:30:00 |         1 |        3 |  3 | AVATAR     | Jake, a paraplegic marine, replaces his brother on the Navi-inhabited Pandora for a corporate mission. He is accepted by the natives as one of their own, but he must decide where his loyalties lie. |      8
#   2 | RODA CINEMA     | Pozeska 15      |q              75 |  3 | 2026-04-24 20:00:00 |         2 |        1 |  1 | Terminator | Movie description...                                                                                                                                                                                  |      7
#   3 | MTS Dvorana     | Decanska 14     |                 |  4 | 2026-04-24 20:00:00 |         3 |        1 |  1 | Terminator | Movie description...                                                                                                                                                                                  |      7
#   3 | MTS Dvorana     | Decanska 14     |                 |  5 | 2026-04-24 17:00:00 |         3 |        3 |  3 | AVATAR     | Jake, a paraplegic marine, replaces his brother on the Navi-inhabited Pandora for a corporate mission. He is accepted by the natives as one of their own, but he must decide where his loyalties lie. |      8
#   2 | RODA CINEMA     | Pozeska 15      |              75 |  6 | 2026-04-24 20:00:00 |         2 |        4 |  4 | The Batman | Batman is called to intervene when the mayor of Gotham City is murdered. Soon, his investigation leads him to uncover a web of corruption, linked to his own dark past.                               |      7