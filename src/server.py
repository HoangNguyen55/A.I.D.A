from http import HTTPStatus
import asyncio
import websockets

ADDRESS = "localhost"
PORT = "5172"

# TODO implement TLS

async def process_request(path, header):
    try:
        # TODO implment database fetching for password hashes, salt, peper, etc...
        auth = header['Authorization']
        if auth:
            return None
    except KeyError:
        message = b'Authorization failed'
    
    return (HTTPStatus.UNAUTHORIZED, 
            {'WWW-Authenticate': 'Basic realm="Access To A.I.D.A"'})

async def handler(websocket):
    async for message in websocket:

        print(message)

        await websocket.send("hi world!")


async def main():
    async with websockets.serve(handler, ADDRESS, PORT, process_request=process_request):
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
