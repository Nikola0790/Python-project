from psycopg2 import connect
from flask import Flask, request, render_template, session

# Exercise 1
# Write a function execute_sql that runs any sql code. The function should take two parameters:
#   database name,
#   SQL query.
# The function should take the sql code given in the parameter and execute it on the given database. 
# sThe function should return a list of results (for queries of the SELECT type), or None.

def execute_sql(db_name, sql_query):
    cnx = connect(dbname=db_name)
    cursor = cnx.cursor()

    results = None

    try:
        cursor.execute(sql_query)
        print("query executed")

        if cursor.description:
            results = cursor.fetchall()
        else:
            cnx.commit() 
        
        cursor.close()
        cnx.close()
    except Exception as e:
        cnx.rollback()
        print(f"PostgreSQL Error: {e}")     
        
    return results

# Exercise 2
# Using Flask, write a program that will display on a page all the products contained in a database named exercises_db.

# Hint: The program should run an SQL query that retrieves all entries from an appropriate table, 
# and then display them on the screen. You can use the code written in the previous exercise.

app = Flask(__name__)
# app.secret_key = "exercises-db"
app.config["SECRET_KEY"] = "Secret-key"

@app.route("/")
def query_db_call():
    return execute_sql("cinemas_db", "SELECT * FROM movies;")


# Exercise 3

@app.route("/movie-form", methods=['GET', 'POST'] )
def get_movie():
    if request.method == "POST":
        movie_name = request.form["movie_name"]
        movie_description = request.form["movie_description"]
        movie_rating = request.form["movie_rating"]

        if not movie_name or not movie_description or not movie_rating:
            return "Error: All fields are required! <a href='/movie-form'>Go Back</a>"
        
        execute_sql("cinemas_db", f"INSERT INTO movies(name, description, rating) VALUES ('{movie_name}', '{movie_description}', '{movie_rating}');")
        return "Movie added successfully! <a href='/movie-form'>Go Back</a>"

    return render_template("form.html")

# Exercise 5
# Using Flask, write a page that:

#   will be available at movie/<movie_id>, the movie_id, being the number that specifies the id of the movie,
#   retrieves information about the movie with the given ID from the database,
#   displays it on the page.

@app.route("/movie/<movie_id>", methods=['GET'])
def get_specific_movie(movie_id):
    movie_data = execute_sql("cinemas_db", f"SELECT * FROM movies WHERE movies.id={movie_id}")
    return movie_data

if __name__ == "__main__":
    app.run(debug=True)