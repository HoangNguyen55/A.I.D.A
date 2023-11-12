import logging
import sqlite3

from .datatype import UserData
from .error import UnknownError, UserDoesNotExist


class DBAccess:
    def __init__(self, db_path: str) -> None:
        self.path = db_path

        self._conn: sqlite3.Connection
        self._cursor: sqlite3.Cursor

        try:
            self._conn = sqlite3.connect(self.path)
            self._cursor = self._conn.cursor()
        except sqlite3.Error as e:
            logging.critical(f"Error connecting to database: {e}")
            exit(1)

    def get_user_password(self, email: str) -> tuple[str, str]:
        """
        Retrieve the UUID and password associated with the given email address from the 'users' table.

        Parameters:
        - email (str): The email address of the user.

        Returns:
        tuple[str, str]: A tuple containing the UUID and password if the user exists, otherwise raises UserDoesNotExist.

        Raises:
        UserDoesNotExist: If the user with the provided email does not exist.
        """
        try:
            self._cursor.execute(
                f"SELECT uuid, password FROM users WHERE email = ?", (email)
            )
            data = self._cursor.fetchone()
            if data:
                return data
        except sqlite3.Error as e:
            logging.error(f"Error getting user: {e}")

        raise UserDoesNotExist

    def get_user_data(self, uuid: str) -> UserData:
        """
        Retrieve the username and system prompt associated with the given UUID from the 'users' table.

        Parameters:
        - uuid (str): The UUID of the user.

        Returns:
        UserData: An instance of UserData containing the username and system prompt.

        Raises:
        UnknownError: If an unexpected error occurs during the retrieval process.
        """
        try:
            self._cursor.execute(
                "SELECT username, system_prompt FROM users WHERE uuid = ?",
                (uuid),
            )
            data = self._cursor.fetchone()[0]
            return UserData(*data)

        except sqlite3.Error as e:
            logging.error(f"Error getting system prompt: {e}")
            raise UnknownError("Something unexpected happened")

    def add_user_pending_approve(
        self, username: str, password: str, email: str
    ) -> None:
        """
        Add a new user to the 'pending_users' table for approval.

        Parameters:
        - username: The username of the new user.
        - password: The password of the new user.
        - email: The email address of the new user.

        Raises:
        UnknownError: If an unexpected error occurs during the insertion process.
        """
        try:
            self._cursor.execute(
                "INSERT INTO pending_users (username, password, email) VALUES (?, ?, ?)",
                (username, password, email),
            )
            self._conn.commit()
        except sqlite3.Error as e:
            logging.error(f"Error adding a new user: {e}")
            raise UnknownError("Something unexpected happened")

    def add_user(self, username: str, password: str, email: str) -> None:
        """
        Add a new user to the 'users' table.

        Parameters:
        - username: The username of the new user.
        - password: The password of the new user.
        - email: The email address of the new user.

        Raises:
        UnknownError: If an unexpected error occurs during the insertion process.
        """
        try:
            self._cursor.execute(
                "INSERT INTO users (username, password, email) VALUES (?, ?, ?)",
                (username, password, email),
            )
            self._conn.commit()
        except sqlite3.Error as e:
            logging.error(f"Error adding a new user: {e}")
            raise UnknownError("Something unexpected happened")

    def _create_pending_table(self):
        self._cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS pending_users (
                username TEXT,
                email TEXT PRIMARY KEY,
                password TEXT
            )
            """
        )
        self._conn.commit()

    def _create_user_table(self):
        self._cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT,
                email TEXT UNIQUE,
                password TEXT,
                admin BOOLEAN,
                system_prompt TEXT
            )
            """
        )
        self._conn.commit()
