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
    email: str
    password: str

    def __init__(self, data: str) -> None:
        data_json = json.loads(data)
        self.connection_type = data_json["connection_type"]
        self.email = data_json["email"]
        self.password = data_json["password"]


@dataclass
class RecieveData:
    user_id: str
    message: str

    def __init__(self, data: str) -> None:
        data_json = json.loads(data)
        self.user_id = data_json["user_id"]
        self.message = data_json["message"]
