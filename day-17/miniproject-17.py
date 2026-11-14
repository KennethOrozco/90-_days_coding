
def get_adult_users(users: list[dict]) -> list[dict]:
    adults = []
    for user in users:
        age = user.get("age")
        name = user.get("name")
        email = user.get("email")
        address = user.get("address")
        if isinstance(address, dict):
            city = address.get("city")
            if not isinstance(city, str):
                city = "Unknown"
        else:
            city = "Unknown"
        if not isinstance(name, str):
            name = "Unknown"
        if not isinstance(email, str):
            email = "Unknown"
        if isinstance(age, int) and not isinstance(age, bool):
            if age >= 18:
                adults.append({"name": name, "age": age, "email": email, "city": city})
    return adults

def count_missing_fields(users: list[dict]) -> int:
    counter = 0
    for user in users:
        age = user.get("age")
        name = user.get("name")
        email = user.get("email")
        address = user.get("address")
        if isinstance(address, dict):
            city = address.get("city")
            if not isinstance(city, str):
                counter += 1
        else:
            counter += 1
        if not isinstance(name, str):
            counter += 1
        if not isinstance(email, str):
            counter += 1
        if not isinstance(age, int) or isinstance(age, bool):
            counter += 1
    return counter
        


def calculate_average_age(users: list[dict]) -> float:
    if not users:
        return 0.0
    return sum(user['age'] for user in users) / len(users)

def display_summary(users: list[dict]) -> None:
    number_of_adults = len(users)
    average_age = calculate_average_age(users)
    print(f"Total adults: {number_of_adults} -- Average age: {average_age:.2f}")
    for user in users:
        print(f"Name: {user['name']}")
        print(f"Age: {user['age']}")
        print(f"Email: {user['email']}")
        print(f"City: {user['city']}")

users = [
    {"id": 1, "name": "Alice", "age": 25, "email": "alice@example.com", "address": {"city": "Boston"}},
    {"id": 2, "name": "Bob", "age": 17, "email": "bob@example.com", "address": {"city": "Chicago"}},
    {"id": 3, "name": "Charlie", "age": None, "email": "charlie@example.com", "address": None},
    {"id": 4, "name": "David", "age": 32, "address": {"city": "Denver"}},
    {"id": 5, "name": "Eve", "age": "29", "email": "eve@example.com", "address": "Seattle"},
    {"id": 6, "name": "Frank", "age": 45, "email": "frank@example.com", "address": {"city": "Miami"}},
    {"id": 7, "name": None, "age": 21, "email": None, "address": {}},
    {"id": 8, "name": "Grace", "age": True, "email": "grace@example.com", "address": {"city": "Austin"}}
]

adults = get_adult_users(users)

display_summary(adults)