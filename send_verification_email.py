import requests

class BackendError(Exception):
    pass
#make some error handling thingies

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

# Example Usage
email = "example@ohs.stanford.edu"

try:
    result = post_user_verify(email)
    print("Verification email sent:", result)
except BackendError as e:
    print(e)
