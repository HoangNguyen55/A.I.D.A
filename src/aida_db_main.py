import logging
import mysql
from mysql.connector import MySQLConnection
from connect_db import read_db_config


class Aida_DB:

    def __init__(self):
        self.db_config = read_db_config()
        self.conn = None  # connection obj
        self.cursor = None  # cursor obj
        # Connect to the database
        self.connect_to_database()

    def connect_to_database(self) -> None:
        # To create a db connection
        try:
            self.conn = MySQLConnection(**self.db_config)
            # Create a cursor object to interact with the database
            self.cursor = self.conn.cursor()
        except mysql.connector.Error as err:
            logging.critical(f"Something went wrong: {err.msg}")

    def create_table(self):
        """ Creates a new table with the given name. """
        query = """
                CREATE TABLE IF NOT EXISTS users (
                    idusers INT AUTO_INCREMENT PRIMARY KEY,
                    username VARCHAR(100) UNIQUE,
                    password VARCHAR(100),
                    admin TINYINT(1) DEFAULT 0,
                    email VARCHAR(100) UNIQUE,
                    system_prompt VARCHAR(500) DEFAULT 'None'
                );
            """
        try:
            self.cursor.execute(query)
            self.conn.commit()  # save changes
        except mysql.connector.Error as e:
            logging.error(f"Something went wrong: {e.msg}")

    def create_pending_users_table(self) -> None:
        query = f"""CREATE TABLE IF NOT EXISTS pending_users (
                           id_pending_users INT AUTO_INCREMENT PRIMARY KEY,
                           username VARCHAR(100) UNIQUE, 
                           password VARCHAR(100), 
                           admin TINYINT(1) DEFAULT 0,
                           email VARCHAR(100) UNIQUE,
                           system_prompt VARCHAR(500) Default 'None'
                           ); """
        try:
            self.connect_to_database()
            self.cursor.execute(query)
            self.conn.commit()
        except mysql.connector.Error as e:
            logging.error(f"Something went wrong: {e.msg}")

    def read_table_data(self, table_name: str) -> None:
        """Returns all data from users table"""

        try:
            self.connect_to_database()
            self.cursor.execute(f"""SELECT * FROM {table_name}""")
            my_result = self.cursor.fetchall()
            for item in my_result:
                print(f'{item}')
        except mysql.connector.Error as e:
            logging.error(f"Error fetching the database: {e.msg}")

    def add_user(self, username: str, password: str, is_admin: int, email: str, prompt: str = 'None') -> None:
        """ To add a new user
        :param is_admin: If the user has admin privileges. --> 0: FALSE, 1: TRUE
        :param prompt: System prompt
        :return: None
        """
        try:
            self.cursor.execute("INSERT INTO users (username, password, admin, email, system_prompt) VALUES (%s, %s, "
                                "%s, %s, %s)", (username, password, is_admin, email, prompt,))
            self.conn.commit()
        except mysql.connector.Error as e:
            logging.error(f"Error adding a new user: {e.msg}")

    def add_pending_user(self, username: str, password: str, admin: int, email: str) -> None:
        """ This function adds user to pending users' db.
        :param admin: If the user has admin privileges. --> 0: FALSE, 1: TRUE
        """
        try:
            self.cursor.execute("INSERT INTO pending_users (username, password, admin, email) VALUES ("
                                "%s, %s, %s, %s)", (username, password, admin, email))
            self.conn.commit()
        except mysql.connector.Error as e:
            logging.error(f"Error adding a new user: {e.msg}")

    def user_exists(self, username: str, email: str, table_name: str) -> bool:
        """Helper method to determine if user exists"""
        query = f"SELECT 1 FROM {table_name} WHERE username = %s AND email = %s"
        try:
            self.cursor.execute(query, (username, email,))
            result = self.cursor.fetchone()
            if result:
                return True  # User exists
            else:
                return False  # User does not exist
        except mysql.connector.Error as e:
            logging.error(f"Error checking user existence: {e.msg}")
            return False  # Assume an error occurred

    def get_user(self, username: str, email: str, table_name: str) -> object:
        """ To search the user in DB and return their data """
        try:
            self.cursor.execute(f"SELECT * FROM {table_name} WHERE username = %s AND email = %s", (username, email,))
            temp = self.cursor.fetchone()
            if temp:
                return temp
            logging.error(f"No user found with the provided username: {username} and email: {email}")
            return f"No user found with the provided username: {username} and email: {email}"
        except mysql.connector.Error as e:
            logging.error(f"Error: {e.msg}")

    def verify_password(self, username: str, password: str):
        pass

    def delete_user(self, username: str, email: str, table_name: str) -> str:
        query = f"""DELETE FROM {table_name} WHERE username = %s AND email = %s"""
        if self.user_exists(username, email, table_name):
            try:
                self.cursor.execute(query, (username, email, ))
                self.conn.commit()  # save the changes
            except mysql.connector.Error as e:
                logging.error(f"Error deleting user: {e.msg}")
        else:
            return f"Error deleting the user: User {username}, {email} was not found"

    def approve_pending_user(self, username: str, email: str) -> str:
        """ To approve a pending user. The user will be removed from pending users db and moved to main db"""

        if self.user_exists(username, email, 'pending_users'):
            temp = self.get_user(username, email, 'pending_users')
            self.add_user(temp[1], temp[2], temp[3], temp[4])
            self.delete_user(username, email, 'pending_users')
        else:
            logging.error(f"User '{username}' was not found")
            return f"User '{username}' was not found"


if __name__ == '__main__':
    my_db = Aida_DB()
    # create users tables
    my_db.create_table()
    # Create pending users table
    my_db.create_pending_users_table()
    #  add users
    # for i in range(25):
    #     my_db.add_user(f'{i}', '123456789', 0, f'{i}', 'None')
    # print(my_db.get_user('user1', 'email1', 'users'))

    # add pending users
    # for i in range(25):
    #     my_db.add_pending_user(f'{i}', '123456789', 0, f'{i}')

    # Add another pending user and approve their request, move the user to the main DB table.
    # my_db.add_pending_user('51', '115345', 0, '51')
    # my_db.approve_pending_user('51', '51')


