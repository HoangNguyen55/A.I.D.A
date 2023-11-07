from configparser import ConfigParser
import logging
import sqlite3
from .error import UserDoesNotExist


class DBAccess:
    """
    A class for accessing a SQLite database and performing user-related operations.

    This class allows you to connect to a SQLite database and perform operations such as
    retrieving user information and adding pending users for approval.

    Args:
        db_path (str): The path to the SQLite database or a .ini file containing the database path.

    Methods:
        get_user(email: str) -> tuple[str, str, str]:
            Retrieve user information based on their email address.

        get_user_system_prompt(uuid: str) -> None | str:
            Retrieve the system prompt associated with a user by their UUID.

        add_user_pending_approve(username, password, email) -> None:
            Add a new user to the list of pending users for approval.

    Note:
        If the `db_path` ends with ".ini," the database path is extracted from the provided
        .ini file. Otherwise, `db_path` is assumed to be the direct path to the SQLite database.

    Example:
        db = DB_Access("my_database.ini")
        user_info = db.get_user("user@example.com")
        if user_info:
            print("User Info:", user_info)
    """

    def __init__(self, db_path: str) -> None:
        if db_path.endswith("ini"):
            config = ConfigParser()
            config.read(db_path)
            path = config.get("database", "database_path")
        else:
            path = db_path

        self._conn: sqlite3.Connection
        self._cursor: sqlite3.Cursor

        try:
            self._conn = sqlite3.connect(path)
            self._cursor = self._conn.cursor()
        except sqlite3.Error as e:
            logging.critical(f"Error connecting to database: {e}")
            exit(1)

    def get_user(self, email: str) -> tuple[str, str, str]:
        """
        Retrieve user information based on their email address.

        Args:
            email (str): The email address of the user to retrieve.

        Returns:
            tuple[str, str, str]: A tuple containing user information (UUID, username, password).

        Raises:
            UserDoesNotExist: If the user with the provided email does not exist in the database.
        """

        try:
            self._cursor.execute(
                f"SELECT uuid, username, password FROM users WHERE email = ?", (email)
            )
            data = self._cursor.fetchone()
            if data:
                return data
        except sqlite3.Error as e:
            logging.error(f"Error getting user: {e}")

        raise UserDoesNotExist

    def get_user_system_prompt(self, uuid: str) -> None | str:
        """
        Retrieve the system prompt associated with a user from the database.

        Args:
            uuid (str): The unique user identifier (UUID) to retrieve the system prompt for.

        Returns:
            str: The system prompt as a string
        """
        try:
            self._cursor.execute(
                f"SELECT system_prompt FROM users WHERE uuid = ?", (uuid)
            )
            system_prompt = self._cursor.fetchone()[0]
            if system_prompt:
                return system_prompt
        except sqlite3.Error as e:
            logging.error(f"Error getting system prompt: {e}")

        return ""

    def add_user_pending_approve(self, username, password, email) -> None:
        """
        Add a new user to the pending users table in the database for approval.

        Args:
            username (str): The username of the new user.
            password (str): The password of the new user.
            email (str): The email address of the new user.

        Returns:
            None
        """
        try:
            self._cursor.execute(
                "INSERT INTO pending_users (username, password, email) VALUES (?, ?, ?)",
                (username, password, email),
            )
            self._conn.commit()
        except sqlite3.Error as e:
            logging.error(f"Error adding a new user: {e}")
