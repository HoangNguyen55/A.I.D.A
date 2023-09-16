from http import HTTPStatus
from ai import AI
import asyncio
import websockets

ADDRESS = "localhost"
PORT = "5172"
ai: AI

# TODO implement TLS (dont really need it rn tho)

async def process_request(path, header):
    try:
        # TODO implment database fetching for password hashes, salt, peper, etc... to check for creds

        auth = header['Authorization']
        if auth:
            # TODO change the header to pass USERID for handler
            return None
    except KeyError:
        message = b'Authorization failed'
    
    return (HTTPStatus.UNAUTHORIZED, 
            {'WWW-Authenticate': 'Basic realm="Access To A.I.D.A"'})

async def handler(websocket):
    # TODO get user specific AI related settings
    # i.e system prompts, etc...

    async for message in websocket:

        response = ai.feed_input(message)

        await websocket.send(response)


async def main():
    async with websockets.serve(handler, ADDRESS, PORT, process_request=process_request):
        await asyncio.Future()

if __name__ == "__main__":
    # TODO start AI here
    ai = AI()
    asyncio.run(main())
