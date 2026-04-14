create_cinemas_db_command = "CREATE DATABASE cinemas_db;"

# Exercise 3

# Write SQL queries that will do the following operations on the table cinemas_db:
#   add 4 new movies,
#   add one ticket for each movie,
#   select all movies whose names begin with the letter D,
#   select all tickets whose price is greater than 15.30,
#   select all tickets whose number is greater than three.

# Write the queries in variables in the file exercise3.py.

add_new_movies = """INSERT INTO movies (name, description, rating) VALUES ('DUNE: Part One', 'Paul Atreides arrives on Arrakis after his father accepts the stewardship of the dangerous planet. However, chaos ensues after a betrayal as forces clash to control melange, a precious resource.', 8),
('Interstellar', 'When Earth becomes uninhabitable in the future, a farmer and ex-NASA pilot, Joseph Cooper, is tasked to pilot a spacecraft, along with a team of researchers, to find a new planet for humans.', 9),
('AVATAR', 'Jake, a paraplegic marine, replaces his brother on the Navi-inhabited Pandora for a corporate mission. He is accepted by the natives as one of their own, but he must decide where his loyalties lie.', 8), 
('The Batman', 'Batman is called to intervene when the mayor of Gotham City is murdered. Soon, his investigation leads him to uncover a web of corruption, linked to his own dark past.', 7);"""

add_tickets = "INSERT INTO tickets (quantity, price) VALUES (1, 10.00), (1, 17.50), (1, 21.20), (1, 14);"
select_movies_first_letter_d = "SELECT * FROM movies WHERE name LIKE 'D%';"
tickets_price_greater_than = "SELECT * FROM tickets WHERE price > 15.50;"
tickets_number_greater_than_three = "SELECT * FROM tickets WHERE quantity > 3;"
