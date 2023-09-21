import bcrypt
import mysql
from mysql.connector import MySQLConnection
from connect_db import read_db_config


class Aida_DB:

    def __init__(self):
        self.db_config = read_db_config()
        self.conn = None
        self.cursor = None
        # Connect to a database
        self.connect_to_database()

    def connect_to_database(self):
        # To create a db connection
        try:
            print('Connecting to MySQL database...')
            self.conn = MySQLConnection(**self.db_config)
            # Create a cursor object to interact with the database
            self.cursor = self.conn.cursor()
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))

    def read_table_data(self):
        """Returns all data from a users table"""

        try:
            self.cursor.execute("""SELECT * FROM users""")
            my_result = self.cursor.fetchall()
            for item in my_result:
                print(f'{item}')
        except mysql.connector.Error as e:
            print("Error fetching the database: ", e.msg)

    def hash_pw(self, password: str) -> str:
        # Generate a salt and has the password
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed_password.decode('utf-8')

    def add_user(self, username: str, password: str, is_admin: int, email: str, prompt: str = 'None') -> None:
        """
            To add a new user
        :param is_admin: If the user has admin privileges
        :param prompt: System prompt
        :return: None
        """
        # Hash the password
        hashed_password = self.hash_pw(password)
        try:
            self.cursor.execute("INSERT INTO users (username, password, admin, email, system_prompt) VALUES (%s, %s, "
                                "%s, %s, %s)", (username, hashed_password, is_admin, email, prompt,))
            self.conn.commit()
            self.cursor.close()
        except mysql.connector.Error as e:
            print("Error adding a new user: ", e.msg)

    def get_user(self, username: str, email: str) -> object:
        """ To search the user in DB and return their data """
        try:
            self.cursor.execute("SELECT * FROM users WHERE username = %s AND email = %s", (username, email,))
            temp = self.cursor.fetchone()
            self.cursor.close()
            if temp:
                return temp
            return f"No user found with the provided username: {username} and email: {email}"
        except mysql.connector.Error as e:
            print("Error: ", e.msg)

    def verify_password(self, username: str, password: str):
        pass

if __name__ == '__main__':
    my_db = Aida_DB()
    # my_db.add_user('test_user4', 'TEMP_password20123@', 0, 'email022@yahoo.com')
    # my_db.connect_to_database()
    print(my_db.get_user('first-user', 'emal@yahoo.com'))

