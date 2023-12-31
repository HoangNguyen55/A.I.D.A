import dataclasses
from dataclasses import dataclass
import enum


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
    password: str
    email: str

    def __str__(self):
        string = "{"
        fields = dataclasses.fields(self)
        for data in fields:
            string += '"' + data.name + '":'
            string += '"' + getattr(self, data.name) + '",'

        string = string[:-1]
        string += "}"
        return string


@dataclass
class PayLoad:
    intent: PayLoadIntent
    message: str

    def __str__(self):
        string = "{"
        fields = dataclasses.fields(self)
        for data in fields:
            string += '"' + data.name + '":'
            string += '"' + getattr(self, data.name) + '",'

        string = string[:-1]
        string += "}"
        return string
