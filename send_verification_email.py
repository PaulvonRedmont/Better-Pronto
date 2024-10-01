import requests, time

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

# Example Usage
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
