from dataclasses import dataclass
import enum
import json


class ConnectionType(enum.IntEnum):
    LOGIN = 0
    SIGNUP = 1


@dataclass
class Credentials:
    connection_type: ConnectionType
    username: str
    email: str
    password: str

    def __init__(self, data: str) -> None:
        data_json: dict = json.loads(data)
        self.connection_type = data_json["connection_type"]
        self.email = data_json.get("email", "")
        self.username = data_json.get("username", "")
        self.password = data_json["password"]


@dataclass
class UserData:
    username: str
    system_prompt: str
