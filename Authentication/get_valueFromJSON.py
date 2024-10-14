def search_key(data, target_key):
    """
    Recursively search for a key in a nested dictionary and return its value.
    
    :param data: The dictionary to search.
    :param target_key: The key to search for.
    :return: The value associated with the key, or None if the key is not found.
    """
    if isinstance(data, dict):
        for key, value in data.items():
            if key == target_key:
                return value
            elif isinstance(value, dict):
                result = search_key(value, target_key)
                if result is not None:
                    return result
            elif isinstance(value, list):
                for item in value:
                    if isinstance(item, dict):
                        result = search_key(item, target_key)
                        if result is not None:
                            return result
    return None
