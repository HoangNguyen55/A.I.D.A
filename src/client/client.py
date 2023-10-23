import asyncio
from websockets import client
import websockets.exceptions


async def main():
    # authorizations = {"Authorization": "Basic dXNlcm5hbWU6cGFzc3dvcmQ="}
    authorizations = {"Authorization": ""}

    uri = "ws://localhost:5172/login"

    async for websocket in client.connect(uri, extra_headers=authorizations):
        try:
            await asyncio.sleep(1)
            await websocket.send("Hello world")
        except websockets.exceptions.ConnectionClosed as err:
            print(err)
            print("rejected")
            continue
        except KeyboardInterrupt:
            await websocket.close()


if __name__ == "__main__":
    asyncio.run(main())
