def get_adult_users(users: list[dict]) -> list[dict]:
    adults = []
    for user in users:
        age = user.get("age")
        name = user.get("name")
        email = user.get("email")
        if not isinstance(name, str):
            name = "Unknown"
        if not isinstance(email, str):
            email = "Unknown"
        if isinstance(age, int) and not isinstance(age, bool):
            if age >= 18:
                adults.append({"name": name, "age": age, "email": email})
    return adults

def calculate_average_age(users: list[dict]) -> float:
    if not users:
        return 0.0
    return sum(user['age'] for user in users) / len(users)

def display_summary(users: list[dict]) -> None:
    number_of_adults = len(users)
    average_age = calculate_average_age(users)
    print(f"Total adults: {number_of_adults}")
    print(f"Average age: {average_age:.2f}")
    for user in users:
        print(f"Name: {user['name']}")
        print(f"Age: {user['age']}")




users = [
    {"id": 1, "name": "Alice", "age": 25, "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "age": 17, "email": "bob@example.com"},
    {"id": 3, "name": "Charlie", "age": None, "email": "charlie@example.com"},
    {"id": 4, "name": "David", "age": 32},
    {"id": 5, "name": "Eve", "age": "29", "email": "eve@example.com"},
    {"id": 6, "name": "Frank", "age": 45, "email": "frank@example.com"}
]


print(display_summary(get_adult_users(users)))