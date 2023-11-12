import sys
from configargparse import Namespace
from websockets.frames import CloseCode
from websockets.typing import Data
from .ai import AI
from .database import DBAccess
from .error import MessageTooBigError
from .datatype import ConnectionType, Credentials, UserData
import logging
import json
import asyncio
from websockets.server import WebSocketServerProtocol, serve
from argon2 import PasswordHasher
from argon2.exceptions import VerificationError

CLI_OPTIONS: Namespace
DB: DBAccess
PASSHASH = PasswordHasher()

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
            uuid, hash_password = DB.get_user_password(creds.email)
            PASSHASH.verify(creds.password, hash_password)
            user_data = DB.get_user_data(uuid)
            logging.debug(f"Connection logged in with name: {creds.email}")
            await handle_data(websocket, user_data)

        elif creds.connection_type == ConnectionType.SIGNUP:
            logging.debug(f"New connection is signing up with the email: {creds.email}")
            if CLI_OPTIONS.auto_approve_signup:
                DB.add_user(creds.username, creds.password, creds.email)
                await websocket.close(
                    CloseCode.TRY_AGAIN_LATER,
                    "Sign up complete, please login again",
                )
            else:
                DB.add_user_pending_approve(creds.username, creds.password, creds.email)
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
    except Exception as err:
        logging.error(f"Unknown error happened: {str(err)}")
        await websocket.close(CloseCode.INTERNAL_ERROR)


async def handle_data(websocket: WebSocketServerProtocol, user_data: UserData):
    await websocket.send(f"Good morning: {user_data.username}")
    async for message in websocket:
        msg = check_data(message)
        logging.debug(f"Message from {user_data.username} recieved: {msg}")
        response = AI.feed_input(msg, user_data.system_prompt)
        logging.info(f"AI responses: {response}")


async def start_server(cli_options: Namespace):
    global CLI_OPTIONS, DB
    CLI_OPTIONS = cli_options
    DB = DBAccess(cli_options.db_path)

    async with serve(handle_connection, cli_options.host_address, cli_options.port):
        await asyncio.Future()
