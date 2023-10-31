from server.database.aida_db_main import Aida_DB

database = Aida_DB()
database.create_pending_users_table()
database.connect_to_database()


def test_add_user():
    exist = database.user_exists("test", "test@example.com", "pending_users")
    assert exist == False, "The user should not exist yet"
    database.add_pending_user("test", "1234", "test@example.com")
    exist = database.user_exists("test", "test@example.com", "pending_users")
    assert exist == True, "The user should exist"
