import asyncio
import websockets

ADDRESS = "localhost"
PORT = "5172"


async def handler(websocket):
    async for message in websocket:

        print(message)

        await websocket.send("hi world!")


async def main():
    async with websockets.serve(handler, ADDRESS, PORT):
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
