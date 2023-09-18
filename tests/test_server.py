import sys, os
script_dir = os.path.dirname( __file__ )
mymodule_dir = os.path.join( script_dir, '..', 'src')
sys.path.append( mymodule_dir )

import pytest
from http import HTTPStatus
from websockets.datastructures import Headers
from server import process_request  

pytest_plugins = ('pytest_asyncio',)

@pytest.mark.asyncio
async def test_login_endpoint_pass():
    # Prepare a mock Headers object with Authorization header
    headers = Headers()
    # base64("username:password")
    headers["Authorization"] = "Basic dXNlcm5hbWU6cGFzc3dvcmQ="  

    # Call the process_request function to simulate a request to /login
    response = await process_request("/login", headers)
    assert response == None, "Should pass the login"


@pytest.mark.asyncio
async def test_login_endpoint_fail():
    # Prepare a mock Headers object with Authorization header
    headers = Headers()
    # Call the process_request function to simulate a request to /login
    response = await process_request("/login", headers)
    assert response != None, "Should fail the login"

    response_status, _, _ = response
    # Check the expected behavior
    assert response_status == HTTPStatus.UNAUTHORIZED, "Should be unauthorized"
