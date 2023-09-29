from database.aida_db_main import Aida_DB

database = Aida_DB()
database.create_table()
database.create_pending_users_table()
database.connect_to_database()


def test_add_user():
    exist = database.user_exists("test", "test@example.com", "users")
    assert exist == False, "The user should not exist yet"
    database.add_user("test", "1234", False, "test@example.com")
    exist = database.user_exists("test", "test@example.com", "users")
    assert exist == True, "The user should exist"
