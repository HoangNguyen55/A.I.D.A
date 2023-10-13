import logging
import sqlite3
from connect_db import read_db_config


class Aida_DB:
    def __init__(self):
        self.db_config = read_db_config()  # SQLite database file
        self.conn = None
        self.cursor = None
        self.connect_to_database()

    def connect_to_database(self) -> None:
        try:
            self.conn = sqlite3.connect(self.db_config)
            self.cursor = self.conn.cursor()
        except sqlite3.Error as e:
            logging.critical(f"Something went wrong: {e}")

    def create_pending_users_table(self) -> None:
        """ Creates a 'pending_users' table in the database if it doesn't already exist. """
        query = """
                CREATE TABLE IF NOT EXISTS pending_users (
                    id_pending_users INTEGER PRIMARY KEY AUTOINCREMENT,
                    firstname VARCHAR(100),
                    lastname VARCHAR(100), 
                    username VARCHAR(100) UNIQUE, 
                    password VARCHAR(100), 
                    admin INTEGER DEFAULT 0,
                    email TEXT UNIQUE
                );
        """
        try:
            self.connect_to_database()
            self.cursor.execute(query)
            self.conn.commit()
        except sqlite3.Error as e:
            logging.error(f"Something went wrong: {e}")

    def read_table_data(self, table_name: str):
        """
            Reads and prints all data from a specified table in the database.
        :param table_name: The name of the table to read data from.
        """

        try:
            self.connect_to_database()
            self.cursor.execute(f"SELECT * FROM {table_name}")
            my_result = self.cursor.fetchall()
            for item in my_result:
                print(item)
        except sqlite3.Error as e:
            logging.error(f"Error fetching the database: {e}")

    def add_pending_user(self, first_name: str, last_name: str, username: str, password: str, email: str) -> None:
        try:
            self.cursor.execute(
                "INSERT INTO aida_admin_app_pendinguser (first_name, last_name, username, password, email) VALUES (?, "
                "?, ?, ?, ?)",
                (first_name, last_name, username, password, email),
            )
            self.conn.commit()
        except sqlite3.Error as e:
            logging.error(f"Error adding a new user: {e}")

    def user_exists(self, username: str, email: str, table_name: str) -> bool:
        query = f"SELECT 1 FROM {table_name} WHERE username = ? AND email = ?"
        try:
            self.cursor.execute(query, (username, email))
            result = self.cursor.fetchone()
            if result:
                return True
            else:
                return False
        except sqlite3.Error as e:
            logging.error(f"Error checking user existence: {e}")
            return False

    def get_user(self, username: str, email: str, table_name: str) -> sqlite3.Row:
        try:
            self.cursor.execute(
                f"SELECT * FROM {table_name} WHERE username = ? AND email = ?",
                (username, email),
            )
            temp = self.cursor.fetchone()
            if temp:
                return temp

            logging.error(
                f"No user found with the provided username: {username} and email: {email}"
            )
        except sqlite3.Error as e:
            logging.error(f"Error: {e}")

        raise Exception(
            f"No user found with the provided username: {username} and email: {email}"
        )

    def delete_user(self, username: str, email: str, table_name: str) -> None:
        query = f"DELETE FROM {table_name} WHERE username = ? AND email = ?"
        if self.user_exists(username, email, table_name):
            try:
                self.cursor.execute(query, (username, email))
                self.conn.commit()
            except sqlite3.Error as e:
                logging.error(f"Error deleting user: {e}")
        else:
            raise Exception(f"Error deleting the user: User {username}, {email} was not found")

    def approve_pending_user(self, username: str, email: str) -> None:
        """To approve a pending user. The user will be removed from pending users db and moved to main db"""
        if self.user_exists(username, email, "pending_users"):
            temp = self.get_user(username, email, "pending_users")
            self.add_user(temp[1], temp[2], temp[3], temp[4])
            self.delete_user(username, email, "pending_users")
        else:
            logging.error(f"User '{username}' was not found")
            raise Exception(f"User '{username}' was not found")


if __name__ == "__main__":
    my_db = Aida_DB()
    # my_db.read_table_data('aida_admin_app_pendinguser')
    # Add users, pending users, and approve a pending user as needed.
