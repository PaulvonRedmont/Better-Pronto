import requests
import logging
import time

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class BackendError(Exception):
    pass

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

def get_device_info():
    return {
        "browsername": "firefox",
        "browserversion": "130.0.0",
        "osname": "macOS",
        "type": "WEB",
        "uuid": "314c9314-d5e5-4ae4-84e2-9f2f3938ca28",
        "osversion": "10.15.6",
        "appversion": "1.0.0"
    }

def token_login(token, device_info):
    url = "https://accounts.pronto.io/api/v1/user.tokenlogin"  # Adjusted URL
    payload = {
        "login_tokens": [token],
        "device": device_info
    }

    logger.info(f"Payload being sent: {payload}")
    
    try:
        response = requests.post(url, json=payload)
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
    token = input("Please enter the verification code you received: ")

    device_info = get_device_info()
    result = token_login(token, device_info)
    if result:
        logger.info(f"User authenticated: {result}")
    else:
        logger.error("Authentication failed")

if __name__ == "__main__":
    main()
