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
