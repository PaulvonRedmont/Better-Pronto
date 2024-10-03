import requests
import logging
import time

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class BackendError(Exception):
    pass

class DeviceInfo:
    def __init__(self, browsername, browserversion, osname, type, uuid, osversion, appversion):
        self.browsername = browsername
        self.browserversion = browserversion
        self.osname = osname
        self.type = type
        self.uuid = uuid
        self.osversion = osversion
        self.appversion = appversion

class TokenLoginRequest:
    def __init__(self, login_tokens, device):
        self.login_tokens = login_tokens
        self.device = device.__dict__

def post_user_verify(email):
    url = "https://accounts.pronto.io/api/v1/user.verify"
    payload = {"email": email}
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        raise BackendError(f"HTTP error occurred: {http_err}")
    except Exception as err:
        raise BackendError(f"An error occurred: {err}")

def token_login(email, code):
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
    request_payload = TokenLoginRequest([code], device_info)

    logger.info(f"Payload being sent: {request_payload.__dict__}")

    try:
        response = requests.post(url, json=request_payload.__dict__)
        response.raise_for_status()
        logger.info("Login successful")
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        logger.error(f"HTTP error occurred: {http_err} - Response: {http_err.response.text}")
    except requests.exceptions.ConnectionError as conn_err:
        logger.error(f"Connection error occurred: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        logger.error(f"Timeout error occurred: {timeout_err}")
    except requests.exceptions.RequestException as req_err:
        logger.error(f"An error occurred: {req_err}")
    return None

def main():
    email = "example@ohs.stanford.edu"

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
        print(e)
        return

    # Prompting the user to enter the verification code
    code = input("Please enter the verification code you received: ")

    result = token_login(email, code)
    if result:
        logger.info(f"User authenticated: {result}")
        token = result.get('users', [{}])[0].get('login_token')
        if token:
            logger.info(f"Received login token: {token}")
            # Save token for future use
            with open("login_token.txt", "w") as file:
                file.write(token)
        else:
            logger.error("Login token missing in the response")
    else:
        logger.error("Authentication failed")

if __name__ == "__main__":
    main()
