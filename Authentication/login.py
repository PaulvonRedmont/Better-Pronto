import requests
import logging
import time
from dataclasses import dataclass, asdict

# Dataclasses for the response and structure of the request payload
@dataclass
class DeviceInfo:
    browsername: str
    browserversion: str
    osname: str
    type: str

class BackendError(Exception):
    pass

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def token_login(email, verification_code):
    url = "https://accounts.pronto.io/api/v3/user.login"
    device_info = DeviceInfo(
        browsername="Firefox",
        browserversion="130.0.0",
        osname="Windows",
        type="WEB"
    )
    request_payload = {
        "email": email,
        "code": verification_code,
        "device": asdict(device_info)
    }
    
    headers = {
        "Content-Type": "application/json"
    }

    logger.info(f"Payload being sent: {request_payload}")

    try:
        response = requests.post(url, json=request_payload, headers=headers)
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

email = "paul257@ohs.stanford.edu"

def main():
    verification_code = input("Please enter the verification code you received: ").strip()
    try:
        result = token_login(email, verification_code)
        if result.get("ok"):
            logger.info(f"User authenticated: {result}")
            pronto_api_token = result.get('users', [{}])[0].get('login_token')
            if pronto_api_token:
                logger.info(f"Received login token: {pronto_api_token}")
                try:
                    with open(r"C:\Users\paul\Desktop\Better Pronto\login_token.txt", "w") as file:
                        file.write(pronto_api_token)
                except IOError as io_err:
                    logger.error(f"File write error: {io_err}")
            else:
                logger.error("Login token not found in response")
        else:
            logger.error(f"Authentication failed: {result.get('error', 'Unknown error')}")
    except BackendError as e:
        logger.error(e)

if __name__ == "__main__":
    main()