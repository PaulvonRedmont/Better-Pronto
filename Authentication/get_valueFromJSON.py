import json

def get_logintoken(file_path):
    try:
        # Open the file and read the contents
        with open(file_path, 'r') as file:
            data = json.load(file)

        # Access the logintoken
        logintoken = data['users'][0]['logintoken']
        return logintoken

    except FileNotFoundError:
        return "File not found."
    except json.JSONDecodeError:
        return "Error decoding JSON."
    except (KeyError, IndexError):
        return "Logintoken not found."

# Example usage
file_path = r'C:\Users\paul\Desktop\Better Pronto\dictionary_response.txt'
token = get_logintoken(file_path)
print("Login Token:", token)
