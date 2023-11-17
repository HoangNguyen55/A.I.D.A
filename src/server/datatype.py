from dataclasses import dataclass
import enum
import json


class ConnectionType(str, enum.Enum):
    LOGIN = "login"
    SIGNUP = "signup"


class PayLoadIntent(str, enum.Enum):
    UPDATE_USER_DATA = "update"
    CHAT = "chat"


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


@dataclass
class PayLoad:
    intent: PayLoadIntent
    message: str

    def __init__(self, data: str) -> None:
        data_json: dict = json.loads(data)
        self.intent = data_json["intent"]
        self.message = data_json["message"]
