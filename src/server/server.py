import logging
import json
from configargparse import Namespace
from websockets.frames import CloseCode
from websockets.typing import Data
from websockets.sync.server import serve, ServerConnection
from .ai import AI
from .database import DBAccess
from .error import UserDoesNotExist
from .datatype import ConnectionType, Credentials, PayLoad, PayLoadIntent, UserData
from argon2 import PasswordHasher
from argon2.exceptions import VerificationError

CLI_OPTIONS: Namespace
DB: DBAccess
PASSHASH = PasswordHasher()


def check_data(data: Data) -> str:
    if not isinstance(data, str):
        raise NotImplementedError("Only string are accept")

    return data


def handle_connection(websocket: ServerConnection):
    # the first message to recieve should be credentials
    try:
        logging.info("Recieving new connection, trying to authenticate")
        data = check_data(websocket.recv())
        creds = Credentials(data)
        logging.debug(f"New connection purpose: {creds.connection_type}")

        if creds.connection_type == ConnectionType.LOGIN:
            uuid, hash_password = DB.get_user_password(creds.email)
            logging.debug(hash_password)
            PASSHASH.verify(hash_password, creds.password)
            user_data = DB.get_user_data(uuid)
            if user_data.system_prompt is None:
                user_data.system_prompt = ""
            logging.debug(f"Connection logged in with name: {creds.email}")
            handle_data(websocket, user_data)

        elif creds.connection_type == ConnectionType.SIGNUP:
            logging.debug(f"New connection is signing up with the email: {creds.email}")
            hashed_password = PASSHASH.hash(creds.password)
            if CLI_OPTIONS.auto_approve_signup:
                DB.add_user(creds.username, hashed_password, creds.email)
                websocket.close(
                    CloseCode.TRY_AGAIN_LATER,
                    "Sign up complete, please login again",
                )
            else:
                DB.add_user_pending_approve(
                    creds.username, hashed_password, creds.email
                )
                websocket.close(
                    CloseCode.TRY_AGAIN_LATER,
                    "Sign up complete, please wait for admin approval",
                )
        else:
            raise NotImplementedError("Connection type unknown")
    except (VerificationError, UserDoesNotExist) as err:
        logging.info(f"Connection fail to authenticate: {str(err)}")
        websocket.close(
            CloseCode.INVALID_DATA,
            "Wrong password or account not yet approves",
        )
    except NotImplementedError as err:
        logging.info(f"Connection fail to authenticate: {str(err)}")
        websocket.close(CloseCode.UNSUPPORTED_DATA, str(err))
    except (json.JSONDecodeError, KeyError) as err:
        logging.info(f"Connection fail: {str(err)}")
        websocket.close(CloseCode.UNSUPPORTED_DATA, "Data recieved are unsupported")


def handle_data(websocket: ServerConnection, user_data: UserData):
    websocket.send(f"Good morning: {user_data.username}")
    for message in websocket:
        payload = PayLoad(check_data(message))
        if payload.intent == PayLoadIntent.UPDATE_USER_DATA:
            # TODO update user data
            continue
        logging.debug(f"Message from {user_data.username} recieved: {payload}")
        # TODO, build the prompt from the previous prompt
        response = AI.feed_input(payload.message, user_data.system_prompt)
        websocket.send(response)


def start_server(cli_options: Namespace):
    global CLI_OPTIONS, DB
    CLI_OPTIONS = cli_options
    DB = DBAccess(cli_options.db_path)
    logging.info("AIDA websocket server started.")

    with serve(handle_connection, cli_options.host_address, cli_options.port) as server:
        server.serve_forever()
