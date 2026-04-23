create_db_command = "CREATE DATABASE exercises_db;"

# Write SQL queries to populate each table in the database named exercises_db 
# with at least several entries. Write the queries in the file exercise1.py.

# Step 1
open_sql_shell = "psql postgres"
# Step 2
list_all_databases = '\l'
# Step 3
connect_to_database = '\c exercises_db'
# Step 4
list_all_tables = '\dt'
# Step 5
show_table_structure = '\d customers'
# Step 6
add_new_data = "INSERT INTO customers (id, name, surname) VALUES (1, 'Nikola', 'Drcalic');"
# table products
# INSERT INTO products (name, description, price) VALUES ('RAM 16GB DDR4', 'High-speed 3200MHz dual-channel memory kit', 85.50),('NVMe SSD 1TB', 'Gen4 x4 M.2 Internal Solid State Drive', 55.00);


# Write a query that will delete a product with id 1. Write the query in the file exercise1.py.
delete_product = "DELETE FROM products WHERE id = 1;"

# Add to the Products table a column that stores the rating of the given product (numeric value with two decimal places). 
# Write the query in the file exercise1.py.
add_column = "ALTER TABLE products ADD rating NUMERIC (1,2);"

# Deleting a column
delete_column = "ALTER TABLE table_name DROP COLUMN column_name;"

# Deleting table & database commands
delete_table = "DROP TABLE table_name;"
remove_database = "DROP DATABASE db_name;"

# Exercise - Link the tables Products and Orders with a many-to-many relationship. 
# Write some queries that link products to orders.

# Step 1
create_join_table = "CREATE TABLE order_items (id serial NOT NULL, order_id int NOT NULL, product_id int NOT NULL, PRIMARY KEY(id), FOREIGN KEY(order_id) REFERENCES orders(id), FOREIGN KEY(product_id) REFERENCES products(id));"
# Step 2
add_data_to_join_table = "INSERT INTO order_items(order_id, product_id) VALUES(1,1),(2,1),(2,2),(3,2),(3,3);"
# Step 3
show_many_to_many_relationship = "SELECT * FROM orders JOIN order_items ON orders.id=order_items.order_id JOIN products ON products.id=order_items.product_id;"


#  id |                     description                      | id | order_id | product_id | id |     name      |                description                 | price  | rating
# ----+------------------------------------------------------+----+----------+------------+----+---------------+--------------------------------------------+--------+--------
#   1 | Customer order for PC build: Motherboard and RAM kit |  6 |        1 |          1 |  1 | Test product  | Test product description                   | 125.00 |   0.05
#   2 | Express shipping requested for NVMe SSD upgrade      |  7 |        2 |          1 |  1 | Test product  | Test product description                   | 125.00 |   0.05
#   2 | Express shipping requested for NVMe SSD upgrade      |  8 |        2 |          2 |  2 | RAM 16GB DDR4 | High-speed 3200MHz dual-channel memory kit |  85.50 |
#   3 | Bulk order for office workstation components         |  9 |        3 |          2 |  2 | RAM 16GB DDR4 | High-speed 3200MHz dual-channel memory kit |  85.50 |
#   3 | Bulk order for office workstation components         | 10 |        3 |          3 |  3 | NVMe SSD 1TB  | Gen4 x4 M.2 Internal Solid State Drive     |  55.00 |