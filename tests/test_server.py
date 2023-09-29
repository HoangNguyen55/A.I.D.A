import pytest
from http import HTTPStatus
from websockets.datastructures import Headers
from server import process_request

pytest_plugins = ("pytest_asyncio",)


@pytest.mark.asyncio
async def test_process_request_no_auth():
    headers = Headers()
    # Call the process_request function to simulate a request to /login
    response = await process_request("", headers)
    assert response != None, "Should be rejects"

    response_status, response_header, response_body = response
    assert response_status == HTTPStatus.UNAUTHORIZED, "Should be unauthorized"

    assert response_header == {"WWW-Authenticate": 'Basic realm="Access To A.I.D.A"'}

    assert response_body == b"Authorization field is missing"


@pytest.mark.asyncio
async def test_process_request_wrong_path():
    headers = Headers()
    # base64("username:password")
    headers["Authorization"] = "Basic dXNlcm5hbWU6cGFzc3dvcmQ="

    response = await process_request("/doest_exist", headers)
    assert response != None, "Should be rejects"

    response_status, _, response_body = response
    assert response_status == HTTPStatus.NOT_FOUND, "Should be unauthorized"
    assert response_body == b"Path does not exist"


@pytest.mark.asyncio
async def test_login_wrong_account():
    headers = Headers()
    headers["Authorization"] = "Basic dXNlcm5hbWU6d3JvbmdfcGFzc3dvcmQ="
    response = await process_request("/login", headers)
    assert response != None, "Should fail the login"

    response_status, _, response_body = response
    assert response_status == HTTPStatus.UNAUTHORIZED, "Should be unauthorized"
    assert response_body == b"Account does not exist"


@pytest.mark.asyncio
async def test_login_pass():
    headers = Headers()
    headers["Authorization"] = "Basic dXNlcm5hbWU6cGFzc3dvcmQ="

    response = await process_request("/login", headers)
    assert response == None, "Should pass the login"


@pytest.mark.asyncio
async def test_signup():
    headers = Headers()
    headers["Authorization"] = "Basic dXNlcm5hbWU6cGFzc3dvcmQ="

    response = await process_request("/signup", headers)
    assert response != None, "Should fail the login"

    response_status, _, response_body = response
    assert response_status == HTTPStatus.ACCEPTED, "Should be accepted"
    assert (
        response_body
        == b"Your sign up request have been recieved\nPlease wait for admin approval"
    )
