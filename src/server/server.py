import sys
from websockets.frames import CloseCode
from websockets.typing import Data
from .ai import AI
from .database.access import DBAccess
from .error import MessageTooBigError
from .datatype import ConnectionType, Credentials, RecieveData
import logging
import json
import asyncio
import secrets
from websockets.server import WebSocketServerProtocol, serve
from argon2 import PasswordHasher
from argon2.exceptions import VerificationError, VerifyMismatchError

PASSHASH = PasswordHasher()
DB = DBAccess("db_config.ini")

# 1 mebibyte
MAX_DATA_SIZE = 1048576


def check_data(data: Data) -> str:
    if sys.getsizeof(data) > MAX_DATA_SIZE:
        raise MessageTooBigError("Message are unparseable")
    if not isinstance(data, str):
        raise NotImplementedError("Only string are accept")

    return data


async def handle_connection(websocket: WebSocketServerProtocol):
    # the first message to recieve should be credentials
    try:
        logging.info("Recieving new connection, trying to authenticate")
        data = check_data(await websocket.recv())
        creds = Credentials(data)
        logging.debug(f"New connection purpose: {creds.connection_type}")

        if creds.connection_type == ConnectionType.LOGIN:
            # user_data = DB.get_user(creds.email)
            # PASSHASH.verify(creds.password, user_data[2])
            logging.debug(f"Connection logged in with name: {creds.email}")
            random_token = secrets.token_urlsafe()
            await websocket.send(random_token)
            await handle_data(websocket, random_token)

        elif creds.connection_type == ConnectionType.SIGNUP:
            logging.debug(f"New connection is signing up with the email: {creds.email}")
            await websocket.close(
                CloseCode.TRY_AGAIN_LATER,
                "Sign up complete, please wait for admin approval",
            )
        else:
            raise NotImplementedError("Connection type unknown")
    except json.JSONDecodeError or KeyError or VerificationError as err:
        logging.info(f"Connection fail to authenticate: {str(err)}")
        await websocket.close(
            CloseCode.INVALID_DATA,
            "Wrong password or account not yet approves",
        )
    except NotImplementedError as err:
        logging.info(f"Connection fail to authenticate: {str(err)}")
        await websocket.close(CloseCode.UNSUPPORTED_DATA, str(err))
    except MessageTooBigError as err:
        logging.info(f"Connection fail to authenticate: {str(err)}")
        await websocket.close(CloseCode.MESSAGE_TOO_BIG, str(err))


async def handle_data(websocket: WebSocketServerProtocol, token: str):
    async for message in websocket:
        # data = RecieveData(check_data(message))
        # logging.info(f"Message recieved: {data.message}")
        # response = AI.feed_input(data.message)
        # logging.info(f"AI responses: {message}")
        await websocket.send(token)


async def start_server(address: str, port: int):
    async with serve(handle_connection, address, port):
        await asyncio.Future()
