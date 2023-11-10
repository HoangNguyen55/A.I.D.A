import asyncio
import signal
from websockets import client
import websockets.exceptions


async def start_client(uri: str, end_point: str):
    async with client.connect(uri + end_point) as websocket:
        await websocket.send(
            '{"connection_type": "login", "email": "tester@gmail.com", "password": "password"}'
        )
        # server should send something back for confirming authenication
        print(await websocket.recv())
        while True:
            try:
                prompt = input("Enter your prompt: ")
                await websocket.send(prompt)

                response = await websocket.recv()
                print("AIDA:", response)
            except websockets.exceptions.ConnectionClosed:
                continue
            except KeyboardInterrupt:
                await websocket.close()
