from http import HTTPStatus
from websockets.datastructures import Headers
from ai import AI
import asyncio
from websockets.server import serve

ADDRESS = "localhost"
PORT = 5172
ai: AI


def login(username: str, password: str):
    # TODO implement data fetching for authorization
    if password == True:
        return None

    return (
        HTTPStatus.UNAUTHORIZED,
        {"WWW-Authenticate": 'Basic realm="Access To A.I.D.A"'},
        b"Account does not exist",
    )


def signup(username: str, password: str):
    # TODO hash, salt, pepper, etc.. the password
    # put it in a database of awaiting approval

    return (
        HTTPStatus.ACCEPTED,
        {},
        b"""
        Your sign up request have been recieved\n
        Please wait for admin approval
        """,
    )


# TODO implement TLS (dont really need it rn tho)
async def process_request(path: str, header: Headers):
    try:
        auth = header["Authorization"].split(":")
        username = auth[0].split(" ")[-1]
        password = auth[1]
    except KeyError:
        return (
            HTTPStatus.UNAUTHORIZED,
            {"WWW-Authenticate": 'Basic realm="Access To A.I.D.A"'},
            b"Authorization field is missing",
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
        response = ai.feed_input(message)

        await websocket.send(response)


async def main():
    async with serve(handler, ADDRESS, PORT, process_request=process_request):
        await asyncio.Future()


if __name__ == "__main__":
    # TODO start AI here
    ai = AI("/model")
    asyncio.run(main())
