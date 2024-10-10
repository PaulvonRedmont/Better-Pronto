import json

# Sample response data (scrubbed of sensitive information)
response_data = {
    "ok": True,
    "users": [
        {
            "user": {
                "id": "REDACTED",
                "firstname": "John",
                "lastname": "Doe",
                "username": None,
                "locale": "",
                "lastseen": "REDACTED",
                "profilepic": True,
                "status": 0,
                "created_at": "REDACTED",
                "updated_at": "REDACTED",
                "deactivated_at": None,
                "email_verified_at": "REDACTED",
                "phone_verified_at": None,
                "isverified": False,
                "dropinorder": 0,
                "maxstreams": 10,
                "autotranslate": False,
                "isonline": True,
                "lastpresencetime": "REDACTED",
                "acceptedtos": "REDACTED",
                "sentwelcomemsg": "REDACTED",
                "role": "user",
                "mute": False,
                "muteuntil": None,
                "isbot": 0,
                "fullname": "John Doe",
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
                "profilepicpath": "REDACTED",
                "profilepicurl": "REDACTED",
                "emails": [
                    {
                        "id": "REDACTED",
                        "user_id": "REDACTED",
                        "email": "anonymous@example.com",
                        "isverified": False,
                        "phoneretrycount": 0,
                        "coderetrycount": 0,
                        "created_at": "REDACTED",
                        "updated_at": "REDACTED"
                    }
                ],
                "phones": [],
                "organizations": [
                    {
                        "id": "REDACTED",
                        "name": "Anonymous Organization",
                        "created_at": "REDACTED",
                        "updated_at": "REDACTED",
                        "profilepic": 1,
                        "profilepicupdated": "REDACTED",
                        "tasks_enabled": True,
                        "uuid": "REDACTED",
                        "shortname": "anonymousorg",
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
                        "profilepicurl": "REDACTED",
                        "profilepicpath": "REDACTED"
                    }
                ],
                "organization": {
                    "id": "REDACTED",
                    "name": "Anonymous Organization",
                    "created_at": "REDACTED",
                    "updated_at": "REDACTED",
                    "profilepic": 1,
                    "profilepicupdated": "REDACTED",
                    "tasks_enabled": True,
                    "uuid": "REDACTED",
                    "shortname": "anonymousorg",
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
                    "profilepicurl": "REDACTED",
                    "profilepicpath": "REDACTED"
                }
            },
            "logintoken": "REDACTED",
            "tokenexpiration": "REDACTED"
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
        "User ID": "REDACTED",
        "Name": f"{user_details.get('firstname', '')} {user_details.get('lastname', '')}",
        "Email": "anonymous@example.com",
        "Is Verified": user_details.get("isverified"),
        "Last Seen": "REDACTED",
        "Profile Pic URL": "REDACTED",
        "Organization": "Anonymous Organization",
        "Permissions": user_details.get("permissions"),
        "Login Token": "REDACTED",
        "Token Expiration": "REDACTED",
    }

    # Save organized data to a file
    with open("user_data.txt", "w") as file:
        file.write("User Information:\n")
        for key, value in organized_data.items():
            file.write(f"{key}: {value}\n")

    print("User data has been saved to user_data.txt")

# Save the scrubbed sample response data to a nicely formatted file
save_user_data_to_file(response_data)
