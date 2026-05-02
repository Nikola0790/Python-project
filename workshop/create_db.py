from psycopg2 import connect, errors

CREATE_DB = "CREATE DATABASE workshop;"
CREATE_USER_TABLE = """CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255) UNIQUE,
    hashed_password VARCHAR(80)
    );
"""
CREATE_MESSAGES_TABLE = """CREATE TABLE messages (
    id SERIAL PRIMARY KEY,
    from_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    to_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    text TEXT,
    creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
"""

DB_USER = "nikola"
DB_NAME = "postgres"
DB_HOST = "localhost"

try:
    cnx = connect(user=DB_USER, host=DB_HOST, database=DB_NAME)
    cnx.autocommit = True
    cursor = cnx.cursor()
    try:
        cursor.execute(CREATE_DB)
        print(f"Database '{DB_NAME}' created successfully.")
    except errors.DuplicateDatabase:
        print(f"Warning: Database '{DB_NAME}' already exists")
    cnx.close()
except errors.OperationalError as e:
    print(f"Could not connect to {DB_HOST} as user {DB_USER}.")
    print(f"Error detail: {e}")

try:
    cnx = connect(database="workshop", user=DB_USER)
    cnx.autocommit = True
    cursor = cnx.cursor()
    try:
        cursor.execute(CREATE_USER_TABLE)
        print("Table users created.")
    except errors.DuplicateTable as e:
        print("Warning: Table exists ", e)

    try:
        cursor.execute(CREATE_MESSAGES_TABLE)
        print("Table messages created.")
    except errors.DuplicateTable as e:
        print("Warning: Table exists ", e)
    cnx.close()
except errors.OperationalError as e:
    print(f"Connection Error: {e}")

    

# DB_CONFIG = {
#     "host": "localhost",
#     "user": "nikola",
#     "dbname": "postgres"
# }

# def create_database(db_name, connection_params):
#     cnx = None
#     cursor = None

#     try:
#         cnx = connect(**connection_params)
#         cnx.autocommit = True
#         cursor = cnx.cursor()
#         ###########################################
#         cursor.execute(f'CREATE DATABASE {db_name}')
#         print(f"Database '{db_name}' created successfully.")
#     except errors.DuplicateDatabase:
#         print(f"Warning: Database '{db_name}' already exists")
#     except errors.OperationalError as e:
#         print(f"Could not connect to {DB_CONFIG['host']} as user {DB_CONFIG['user']}.")
#         print(f"Error detail: {e}")
#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")
#     finally:
#         if cursor:
#             cursor.close()
#         if cnx:
#             cnx.close()
