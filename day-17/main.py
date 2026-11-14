def display_users(users: list[dict]) -> None:
    counter = 0
    for user in users:
        name = user.get('name')
        if not isinstance(name, str):
            name = "Unknown"
            counter += 1
        email = user.get('email')
        if not isinstance(email, str):
            email = "Unknown"
            counter += 1
        address = user.get("address")
        if isinstance(address, dict):
            city = address.get("city")
            if not isinstance(city, str):
                city = "Unknown"
                counter += 1
        else:
            city = "Unknown"
            counter += 1
        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"City: {city}")
    print(f"Miising fields: {counter}")

users = [
    {"name": "Alice", "email": "alice@example.com", "address": {"city": "Boston"}},
    {"name": "Bob", "email": None, "address": None},
    {"name": "Charlie", "email": 12345, "address": "Chicago"},
    {"name": "David", "address": {"city": None}},
    {"name": "Eve", "email": "eve@example.com", "address": {"city": "Seattle"}}
]

display_users(users)