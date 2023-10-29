from http import HTTPStatus
from base64 import b64decode
from websockets.datastructures import Headers
from .ai import AI
import asyncio
from websockets.server import serve
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

ADDRESS = "localhost"
PORT = 5172
PASSHASH = PasswordHasher()


def login(username: str, password: str):
    # TODO implement data fetching for authorization
    hash = "$argon2id$v=19$m=65536,t=3,p=4$YzqRu34w0ZDZ9oF60Xqy1A$pMNUJ57zWywfRs8sNXTDii9BC1FyqlSNnt3bl+0R77U"
    try:
        PASSHASH.verify(hash, password)
    except VerifyMismatchError:
        return (
            HTTPStatus.UNAUTHORIZED,
            {"WWW-Authenticate": 'Basic realm="Access To A.I.D.A"'},
            b"Account does not exist",
        )

    return None


def signup(username: str, password: str):
    hashed_pass = PASSHASH.hash(password)
    # put it in a database of awaiting approval

    return (
        HTTPStatus.ACCEPTED,
        {},
        b"Your sign up request have been recieved\nPlease wait for admin approval",
    )


# TODO implement TLS (dont really need it rn tho)
async def process_request(path: str, header: Headers):
    try:
        authb64 = header["Authorization"].split(" ")[-1]
        auth = b64decode(authb64).decode("utf-8").split(":")
        username = auth[0]
        password = auth[1]
    except KeyError:
        return (
            HTTPStatus.UNAUTHORIZED,
            {"WWW-Authenticate": 'Basic realm="Access To A.I.D.A"'},
            b"Authorization field is missing or unparseable",
        )

    match path:
        case "/login":
            return login(username, password)
        case "/signup":
            return signup(username, password)
        case _:
            return (HTTPStatus.NOT_FOUND, {}, b"Path does not exist")


async def handler(websocket):
    # TODO get user specific AI related settings
    # i.e system prompts, etc...

    async for message in websocket:
        response = AI.feed_input(message)

        await websocket.send(response)


async def main():
    async with serve(handler, ADDRESS, PORT, process_request=process_request):
        await asyncio.Future()


if __name__ == "__main__":
    # TODO start AI here
    asyncio.run(main())
