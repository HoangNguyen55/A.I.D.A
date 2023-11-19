from threading import Thread
from websockets.frames import Close, CloseCode
from websockets.sync.connection import Connection
from websockets.sync.client import connect
from .datatype import Credentials, ConnectionType, PayLoad, PayLoadIntent
from time import sleep
from queue import Queue
import websockets
import getpass

user_input = Queue(1)


def start_client(uri: str):
    sleep_time = 1
    while True:
        try:
            action = getUserAction()
            with connect(uri) as websocket:
                while True:
                    try:
                        if action == ConnectionType.SIGNUP:
                            signup(websocket)
                        elif action == ConnectionType.LOGIN:
                            login(websocket)
                            action = None

                        thread = Thread(
                            target=getUserInput,
                            args=("Enter your prompt: ",),
                            daemon=True,
                        )
                        thread.start()
                        websocket.send(user_input.get())

                        for msg in websocket.recv_streaming():
                            print(msg, end="")
                        print()
                    except websockets.exceptions.ConnectionClosed as err:
                        print()
                        print(err.rcvd)
                        if err.rcvd and (
                            err.rcvd.code == CloseCode.INVALID_DATA
                            or err.rcvd.code == CloseCode.TRY_AGAIN_LATER
                        ):
                            break
                    except KeyboardInterrupt:
                        websocket.close()
                        break
        except ConnectionRefusedError:
            print("Server not started or connection error, trying to reconnect...")
            sleep(sleep_time)
            sleep_time = sleep_time if sleep_time >= 60 else sleep_time * 2


def login(websocket: Connection):
    email = input("Email: ")
    password = getpass.getpass()
    payload = Credentials(ConnectionType.LOGIN, "", password, email)
    websocket.send(str(payload))
    # server should send something back for confirming authenication
    print(websocket.recv())


def signup(websocket: Connection):
    username = input("Username: ")

    password = getpass.getpass()
    confirm_password = getpass.getpass("Confirm Password: ")
    while password != confirm_password:
        print("Password does not match.")
        password = getpass.getpass()
        confirm_password = getpass.getpass("Confirm Password: ")

    email = input("Email: ")
    payload = Credentials(ConnectionType.SIGNUP, username, password, email)
    websocket.send(str(payload))
    # connection should terminate
    websocket.recv()


def getUserInput(prompt: str):
    prompt = input("Enter your prompt: ")
    user_input.put(str(PayLoad(PayLoadIntent.CHAT, prompt)))


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
