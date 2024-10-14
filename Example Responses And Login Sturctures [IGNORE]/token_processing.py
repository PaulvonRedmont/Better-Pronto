import requests
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_token_from_user():
    return input("Enter your login token: ")

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
    url = "https://stanfordohs.pronto.io/v1/user.tokenlogin"  # Example adjusted URL
    payload = {
        "login_tokens": [token],
        "device": device_info
    }
    
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

if __name__ == "__main__":
    token = get_token_from_user()
    device_info = get_device_info()
    result = token_login(token, device_info)
    if result:
        logger.info(f"User authenticated: {result}")
    else:
        logger.error("Authentication failed")
