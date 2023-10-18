import configparser


def read_db_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    database_path = config.get('database', 'database_path')
    return database_path
