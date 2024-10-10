import requests
import logging
import time
from dataclasses import dataclass, asdict
from typing import List, Optional

# Dataclasses for the response and structure of the request payload
@dataclass
class UserInfo:
    id: int
    username: str
    email: str

@dataclass
class LoginUser:
    user: UserInfo
    login_token: str
    token_expiration: str

@dataclass
class UserLoginResponse:
    ok: bool
    users: List[LoginUser]

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class BackendError(Exception):
    pass

@dataclass
class DeviceInfo:
    browsername: str
    browserversion: str
    osname: str
    type: str
    uuid: str
    osversion: str
    appversion: str

@dataclass
class TokenLoginRequest:
    login_tokens: List[str]
    device: dict

def post_user_verify(email):
    url = "https://accounts.pronto.io/api/v1/user.verify"
    payload = {"email": email}
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        logger.error(f"HTTP error occurred: {http_err} - Response: {response.text}")
        raise BackendError(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        logger.error(f"Request exception occurred: {req_err}")
        raise BackendError(f"Request exception occurred: {req_err}")
    except Exception as err:
        logger.error(f"An unexpected error occurred: {err}")
        raise BackendError(f"An unexpected error occurred: {err}")

def token_login(verification_code):
    url = "https://accounts.pronto.io/api/v1/user.tokenlogin"
    device_info = DeviceInfo(
        browsername="firefox",
        browserversion="130.0.0",
        osname="macOS",
        type="WEB",
        uuid="314c9314-d5e5-4ae4-84e2-9f2f3938ca28",
        osversion="10.15.6",
        appversion="1.0.0"
    )
    request_payload = TokenLoginRequest([verification_code], asdict(device_info))
    
    # Set headers with authorization
    headers = {
        "Authorization": f"Bearer {verification_code}",
        "Content-Type": "application/json"
    }

    logger.info(f"Payload being sent: {asdict(request_payload)}")

    try:
        response = requests.post(url, json=asdict(request_payload), headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        logger.error(f"HTTP error occurred: {http_err} - Response: {response.text}")
        raise BackendError(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        logger.error(f"Request exception occurred: {req_err}")
        raise BackendError(f"Request exception occurred: {req_err}")
    except Exception as err:
        logger.error(f"An unexpected error occurred: {err}")
        raise BackendError(f"An unexpected error occurred: {err}")

def main():
    email = "paul257@ohs.stanford.edu"

    try:
        print("Requesting verification code for", email)
        request_start_time = time.time()
        result = post_user_verify(email)
        request_end_time = time.time()
        total_time = request_end_time - request_start_time
        print(f"Request took {total_time:.2f} seconds.")
        print("Verification email sent:", result)
        print(f"Please check {email} for the verification code.")
    except BackendError as e:
        logger.error(e)
        return

    # Prompting the user to enter the verification code
    verification_code = input("Please enter the verification code you received: ").strip()

    try:
        result = token_login(verification_code)
        if result:
            logger.info(f"User authenticated: {result}")
            pronto_api_token = result.get('users', [{}])[0].get('login_token')
            if pronto_api_token:
                logger.info(f"Received login token: {pronto_api_token}")
                # Save token for future use
                try:
                    with open("login_token.txt", "w") as file:
                        file.write(pronto_api_token)
                except IOError as io_err:
                    logger.error(f"File write error: {io_err}")
            else:
                logger.error("Login token not found in response")
        else:
            logger.error("Authentication failed")
    except BackendError as e:
        logger.error(e)

if __name__ == "__main__":
    main()
