from psycopg2 import connect
from flask import Flask, request, session

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
app.secret_key = "exercises-db"

@app.route("/")
def query_db_call():
    return execute_sql("cinemas_db", "SELECT * FROM movies;")

if __name__ == "__main__":
    app.run(debug=True)