import bcrypt

class User:
    def __init__(self, username: str = "", password: str = None):
        self._id = -1
        self.username = username
        self._hashed_password = None
        if password is not None:
            self._hashed_password = self._hash_raw_password(password)

    @property
    def id(self):
        return self._id
    
    @property
    def hashed_password(self):
        return self._hashed_password
    
    def _hash_raw_password(self, password: str) -> str:
        #Helper to turn a string into a hashed string.
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    def set_new_password(self, new_password: str):
        self._hashed_password = self._hash_raw_password(new_password)

    @hashed_password.setter
    def hashed_password(self, password):
        self.set_new_password(password)

    def save_to_db(self, cursor):
        if self._id == -1:
            sql = "INSERT INTO users(username, hashed_password) VALUES(%s, %s) RETURNING id;"
            values = (self.username, self.hashed_password)
            cursor.execute(sql, values)
            self._id = cursor.fetchone()[0]
            return True
        else:
            sql = "UPDATE users SET username = %s, hashed_password = %s WHERE id = %s;"
            values = (self.username, self.hashed_password, self.id)
            cursor.execute(sql, values)
            return True
    
    @staticmethod
    def load_user_by_username(cursor, username):
        sql = "SELECT * FROM users WHERE username = %s;"
        cursor.execute(sql, (username,))
        data = cursor.fetchone()

        if data:
            id_, username, hashed_password = data
            loaded_user = User(username)
            loaded_user._id = id_
            loaded_user._hashed_password = hashed_password
            return loaded_user
    
    @staticmethod
    def load_user_by_id(cursor, id_):
        sql = "SELECT * FROM users WHERE id=%s;"
        cursor.execute(sql, (id_,))
        data = cursor.fetchone()

        if data:
            id_, username, hashed_password = data
            loaded_user = User(username)
            loaded_user._id = id_
            loaded_user._hashed_password = hashed_password
            return loaded_user

    @staticmethod
    def load_all_users(cursor):
        users = []
        sql = "SELECT * FROM users;"
        cursor.execute(sql)
        data = cursor.fetchall()
        
        for row in data:
            id_, username, hashed_password = row
            loaded_user = User()
            loaded_user._id = id_
            loaded_user.username = username
            loaded_user._hashed_password = hashed_password
            users.append(loaded_user)
        return users

    def delete(self, cursor):
        sql = "DELETE FROM users WHERE id=%s;"
        cursor.execute(sql, (self.id))
        self._id = -1
        return True

class Message():
    def __init__(self, from_id: int, to_id: int, text: str):
        self._id = -1
        self.from_id = from_id
        self.to_id = to_id
        self.text = text
        self._creation_date = None
    
    @property
    def id(self):
        return self._id
    
    @property
    def creation_date(self):
        return self._creation_date
    
    def save_to_db(self, cursor):
        if self._id == -1:
            sql = "INSERT INTO messages(from_id, to_id, text) VALUES(%s, %s, %s) RETURNING id, creation_date;"
            values = (self.from_id, self.to_id, self.text)
            cursor.execute(sql, values)
            self._id, self._creation_date = cursor.fetchone()
            return True
        else:
            sql = "UPDATE messages SET to_id=%s, from_id=%s, text=%s WHERE id=%s"
            values = (self.self.from_id, self.to_id, self.text, self.id)
            cursor.execute(sql, values)
            return True

    @staticmethod
    def load_all_messages(cursor, user_id=None):
        if user_id:
            sql = "SELECT * FROM messages WHERE to_id=%s;"
            cursor.execute(sql, (user_id,))
        else:
            sql = "SELECT * FROM messages;"
            cursor.execute(sql)
        
        data = cursor.fetchall()
        messages = []
        for row in data:
            id_, from_id, to_id, text, creation_date = row
            loaded_message = Message(from_id, to_id, text)
            loaded_message._id = id_
            loaded_message._creation_date = creation_date
            messages.append(loaded_message)
        return messages