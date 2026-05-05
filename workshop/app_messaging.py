import argparse
import bcrypt
from psycopg2 import connect
from models import Message, User

def sending_message(cursor, from_id, to, message_content):
    recipient = User.load_user_by_username(cursor, to)
    if recipient:
        if len(message_content) <= 255:
            message = Message(from_id, recipient.id, message_content)
            message.save_to_db(cursor)
            print("Message send")
        else:
            print("Message is too long. Max characters is 255.")
    else:
        print("Recipient doesn't exist!")
         

def listings_messages(cursor, user):
    messages = Message.load_all_messages(cursor, user.id)
    for m in messages:
        print(f"- {m.text}")



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--username", help="The username of the user")
    parser.add_argument("-p", "--password", help="The user's password")
    parser.add_argument("-t", "--to", help="username to which the message will be sent")
    parser.add_argument("-s", "--send", help="message content")
    parser.add_argument("-l", "--list", action="store_true", help="request to list all user messages")

    args = parser.parse_args()
    

    try:
        cnx = connect(database="workshop", user="nikola")
        cnx.autocommit = True
        cursor = cnx.cursor()

        if args.password and args.username:
            user = User.load_user_by_username(cursor, args.username)
            if user and bcrypt.checkpw(args.password.encode('utf-8'), user.hashed_password.encode('utf-8')):
                if args.list:
                    listings_messages(cursor, user)
                elif args.to and args.send:
                    sending_message(cursor, user.id, args.to, args.send)
                else:
                    parser.print_help()
            else:
                print("Incorrect password or User does not exists!")
        else:
            print("username and password are required")
            parser.print_help()

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()