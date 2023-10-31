from http import HTTPStatus
import logging
from base64 import b64decode
from websockets.datastructures import Headers
from .ai import AI
import asyncio
from websockets.server import serve
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

_PASSHASH = PasswordHasher()


def _login(username: str, password: str):
    # TODO implement data fetching for authorization
    hash = "$argon2id$v=19$m=65536,t=3,p=4$YzqRu34w0ZDZ9oF60Xqy1A$pMNUJ57zWywfRs8sNXTDii9BC1FyqlSNnt3bl+0R77U"
    try:
        _PASSHASH.verify(hash, password)
    except VerifyMismatchError:
        return (
            HTTPStatus.UNAUTHORIZED,
            {"WWW-Authenticate": 'Basic realm="Access To A.I.D.A"'},
            b"Account does not exist",
        )

    return None


def _signup(username: str, password: str):
    hashed_pass = _PASSHASH.hash(password)
    # put it in a database of awaiting approval

    return (
        HTTPStatus.ACCEPTED,
        {},
        b"Your sign up request have been recieved\nPlease wait for admin approval",
    )


# TODO implement TLS (dont really need it rn tho)
async def _process_request(path: str, header: Headers):
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
            return _login(username, password)
        case "/signup":
            return _signup(username, password)
        case _:
            return (HTTPStatus.NOT_FOUND, {}, b"Path does not exist")


async def _handler(websocket):
    # TODO get user specific AI related settings
    # i.e system prompts, etc...

    async for message in websocket:
        logging.info(f"Message recieved: {message}")
        response = AI.feed_input(message)
        logging.info(f"AI responses: {message}")
        await websocket.send(response)


async def start_server(address: str, port: int):
    async with serve(_handler, address, port, process_request=_process_request):
        await asyncio.Future()
