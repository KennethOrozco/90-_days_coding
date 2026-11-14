import json

def load_data(file_path):
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Invalid JSON data!")
        return []

def validate_data(data):
    if not isinstance(data, list):
        raise TypeError("Data must be a list")
    return data