import dataclasses
from dataclasses import dataclass
import enum


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
