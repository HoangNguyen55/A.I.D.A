import getpass
from websockets import WebSocketClientProtocol, client
import websockets.exceptions

from .datatype import Credentials, ConnectionType


async def start_client(uri: str):
    while True:
        async with client.connect(uri) as websocket:
            action = getUserAction()
            try:
                if action == ConnectionType.SIGNUP:
                    await signup(websocket)
                elif action == ConnectionType.LOGIN:
                    await login(websocket)

                prompt = input("Enter your prompt: ")
                await websocket.send(prompt)

                response = await websocket.recv()
                print("AIDA:", response)
            except websockets.exceptions.ConnectionClosed as err:
                print()
                print(err)
                continue
            except KeyboardInterrupt:
                await websocket.close()
                break


async def login(websocket: WebSocketClientProtocol):
    email = input("Email: ")
    password = getpass.getpass()
    payload = Credentials(ConnectionType.LOGIN, "", password, email)
    await websocket.send(str(payload))
    # server should send something back for confirming authenication
    print(await websocket.recv())


async def signup(websocket: WebSocketClientProtocol):
    username = input("Username: ")

    password = getpass.getpass()
    confirm_password = getpass.getpass("Confirm Password: ")
    while password != confirm_password:
        print("Password does not match.")
        password = getpass.getpass()
        confirm_password = getpass.getpass("Confirm Password: ")

    email = input("Email: ")
    payload = Credentials(ConnectionType.SIGNUP, username, password, email)
    await websocket.send(str(payload))
    # connection should terminate
    await websocket.recv()


def getUserAction():
    while True:
        try:
            choice = int(input("Enter 1 to sign up or 2 to log in: "))
            if choice == 1:
                return ConnectionType.SIGNUP
            elif choice == 2:
                return ConnectionType.LOGIN
            else:
                print("Invalid choice. Please enter 1 or 2.")
        except ValueError:
            print("Invalid input. Please enter a number (1 or 2).")
