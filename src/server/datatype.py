from dataclasses import dataclass
import enum
import json


class ConnectionType(enum.StrEnum):
    LOGIN = "login"
    SIGNUP = "signup"

    @classmethod
    def _missing_(cls, value: str):
        value = value.lower()
        for member in cls:
            if member.lower() == value:
                return member
        return None


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
