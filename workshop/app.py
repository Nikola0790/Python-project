import argparse
import bcrypt
from psycopg2 import connect, errors
from models import User, Message

def create_user(cursor, username, password):
    print(f"Attempting to create user: {username}")
    if len(password) < 8:
        print("Error: Password must be at least 8 characters long.")

    try:
        new_user = User(username, password)
        new_user.save_to_db(cursor)
    except errors.UniqueViolation:
        print(f"Error: User already exists.")
    print("User created successfully!")

def edit_password(cursor, username, password, new_pass):
    print(f"Attempting to edit user password: {username}")
    user = User.load_user_by_username(cursor, username)

    if user:
        if bcrypt.checkpw(password.encode('utf-8'), user.hashed_password.encode('utf-8')):
            if len(password) < 8:
                print("Error: Password must be at least 8 characters long.")
            else:
                user.set_new_password(new_pass)
                user.save_to_db(cursor)
                print("Password changed.")

def delete_user(cursor, username, password):
    print(f"Attempting to delete user: {username}")
    user = User.load_user_by_username(cursor, username)

    if user:
        if bcrypt.checkpw(password.encode('utf-8'), user.hashed_password.encode('utf-8')):
            user.delete(cursor)
            print("User deleted successfully.")
    else:
        print("Incorrect Password!")

def list_users(cursor):
    users = User.load_all_users(cursor)
    for u in users:
        print(f"- {u}")

def main():
    parser = argparse.ArgumentParser(description="User Menagment System")
    parser.add_argument("-u", "--username", help="The username of the user")
    parser.add_argument("-p", "--password", help="The user's password")
    parser.add_argument("-n", "--new_pass", help="A new password for the user")

    parser.add_argument("-l", "--list", action="store_true", help="Show the list of users")
    parser.add_argument("-d", "--delete", action="store_true", help="Delete the specified user")
    parser.add_argument("-e", "--edit", action="store_true", help="Edit the specified user")
    # Parsing the input
    args = parser.parse_args()

    try:
        conn = connect(database="workshop", user="nikola")
        conn.autocommit = True
        cursor = conn.cursor()

        if args.list:
            list_users(cursor)
        elif args.username and args.password and args.edit and args.new_pass:
            edit_password(cursor, args.username, args.password, args.new_pass)
        elif args.username and args.password and args.delete:
            delete_user(cursor, args.username, args.password)
        elif args.username and args.password:
            create_user(cursor, args.username, args.password)
        else:
            parser.print_help()

        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()