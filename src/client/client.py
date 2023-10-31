import asyncio
import signal
from websockets import client
import websockets.exceptions


async def start_client(uri: str, end_point: str):
    authorizations = {"Authorization": "Basic dXNlcm5hbWU6cGFzc3dvcmQ="}
    # authorizations = {"Authorization": ""}

    async with client.connect(
        uri + end_point, extra_headers=authorizations
    ) as websocket:
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
