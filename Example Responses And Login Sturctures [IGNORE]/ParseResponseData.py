import json

# Sample response data (replace this with your actual response data)
response_data = {
    "ok": True,
    "users": [
        {
            "user": {
                "id": 5302367,
                "firstname": "Paul Eastlund",
                "lastname": "Estrada",
                "username": None,
                "locale": "",
                "lastseen": "2024-10-10 20:12:55",
                "profilepic": True,
                "status": 0,
                "created_at": "2023-08-04 00:44:04",
                "updated_at": "2024-10-10 19:42:37",
                "deactivated_at": None,
                "email_verified_at": "2024-10-05 15:12:52",
                "phone_verified_at": None,
                "isverified": False,
                "dropinorder": 0,
                "maxstreams": 10,
                "autotranslate": False,
                "isonline": True,
                "lastpresencetime": "2024-10-10 19:38:56",
                "acceptedtos": "2024-10-05 15:12:52",
                "sentwelcomemsg": "2023-08-14 18:20:16",
                "role": "user",
                "mute": False,
                "muteuntil": None,
                "isbot": 0,
                "fullname": "Paul Eastlund Estrada",
                "hasactivity": True,
                "inactive": False,
                "language": "en",
                "permissions": {
                    "change_name": "system",
                    "change_email": "system",
                    "change_phone": "system",
                    "remove_user": "system",
                    "change_title": "admin",
                    "change_pronouns": "admin",
                    "change_own_name": False,
                    "change_own_email": False,
                    "change_own_phone": False,
                    "change_own_title": True,
                    "change_own_pronouns": True
                },
                "profilepicpath": "/files/users/5302367/profilepic?pronto_time=1727628951",
                "profilepicurl": "https://files.chat.trypronto.com/files/users/5302367/profilepic?pronto_time=1727628951",
                "emails": [
                    {
                        "id": 5302367,
                        "user_id": 5302367,
                        "email": "paul257@ohs.stanford.edu",
                        "isverified": False,
                        "phoneretrycount": 0,
                        "coderetrycount": 0,
                        "created_at": "2023-08-04 00:44:04",
                        "updated_at": "2024-10-10 19:42:37"
                    }
                ],
                "phones": [],
                "organizations": [
                    {
                        "id": 2245,
                        "name": "Stanford Online High School",
                        "created_at": "2022-05-23 21:21:47",
                        "updated_at": "2024-08-29 21:50:51",
                        "profilepic": 1,
                        "profilepicupdated": "2023-04-25 02:01:06",
                        "tasks_enabled": True,
                        "uuid": "5a688730dade11ec9efe71a87fba95ed",
                        "shortname": "stanfordohs",
                        "announcements_enabled": True,
                        "meetings_enabled": True,
                        "audio_messages_enabled": True,
                        "maxstreams": 10,
                        "imports_enabled": True,
                        "search_enabled": True,
                        "create_api_tokens": "admin",
                        "bubble_membership_cap": 3000,
                        "giphy_rating": "PG-13",
                        "user_title_enabled": False,
                        "user_pronouns_enabled": True,
                        "profilepicurl": "https://files.chat.trypronto.com/files/orgs/2245/profilepic?pronto_time=1682388066",
                        "profilepicpath": "/files/orgs/2245/profilepic?pronto_time=1682388066"
                    }
                ],
                "organization": {
                    "id": 2245,
                    "name": "Stanford Online High School",
                    "created_at": "2022-05-23 21:21:47",
                    "updated_at": "2024-08-29 21:50:51",
                    "profilepic": 1,
                    "profilepicupdated": "2023-04-25 02:01:06",
                    "tasks_enabled": True,
                    "uuid": "5a688730dade11ec9efe71a87fba95ed",
                    "shortname": "stanfordohs",
                    "announcements_enabled": True,
                    "meetings_enabled": True,
                    "audio_messages_enabled": True,
                    "maxstreams": 10,
                    "imports_enabled": True,
                    "search_enabled": True,
                    "create_api_tokens": "admin",
                    "bubble_membership_cap": 3000,
                    "giphy_rating": "PG-13",
                    "user_title_enabled": False,
                    "user_pronouns_enabled": True,
                    "profilepicurl": "https://files.chat.trypronto.com/files/orgs/2245/profilepic?pronto_time=1682388066",
                    "profilepicpath": "/files/orgs/2245/profilepic?pronto_time=1682388066"
                }
            },
            "logintoken": "JoGL7PT0s90jOGs8KscHCDWe44nqdDhv7H9V",
            "tokenexpiration": "2024-10-10 20:46:19"
        }
    ]
}

def save_user_data_to_file(data):
    users = data.get("users", [])
    if not users:
        print("No user data found.")
        return

    # Take the first user (if there are multiple users)
    user_info = users[0]
    user_details = user_info.get("user", {})

    # Organize the data in a dictionary
    organized_data = {
        "User ID": user_details.get("id"),
        "Name": f"{user_details.get('firstname', '')} {user_details.get('lastname', '')}",
        "Email": user_details.get("emails", [{}])[0].get("email"),
        "Is Verified": user_details.get("isverified"),
        "Last Seen": user_details.get("lastseen"),
        "Profile Pic URL": user_details.get("profilepicurl"),
        "Organization": user_details.get("organization", {}).get("name"),
        "Permissions": user_details.get("permissions"),
        "Login Token": user_info.get("logintoken"),
        "Token Expiration": user_info.get("tokenexpiration"),
    }

    # Save organized data to a file
    with open("user_data.txt", "w") as file:
        file.write("User Information:\n")
        for key, value in organized_data.items():
            file.write(f"{key}: {value}\n")

    print("User data has been saved to user_data.txt")

# Save the sample response data to a nicely formatted file
save_user_data_to_file(response_data)