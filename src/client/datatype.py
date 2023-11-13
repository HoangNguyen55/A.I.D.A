import dataclasses
from dataclasses import dataclass
import enum


class ConnectionType(enum.IntEnum):
    LOGIN = 0
    SIGNUP = 1


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
