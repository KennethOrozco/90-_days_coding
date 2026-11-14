import requests

def get_user_id() -> int:
    while True:
        try:
            user_ID = int(input("Enter a user ID: "))
        except ValueError:
            print("Type a number!")
        else:
            return user_ID


def view_user() -> None:
    user_ID = get_user_id()
    url = f"https://jsonplaceholder.typicode.com/users/{user_ID}"
    data = get_json_data(url)
    if data is None:
        print("No data found")
    else:
        print(f"Name: {data['name']}")
        print(f"Email: {data['email']}")
        print(f"City: {data['address']['city']}")
        print(f"Company: {data['company']['name']}")
    

def view_posts() -> None:
    url = "https://jsonplaceholder.typicode.com/posts"
    user_ID = get_user_id()
    data = get_json_data(url, {"userId": user_ID})
    if data is None:
           print("No data found")
    else:
        print(f"Total posts: {len(data)}")
        for post in data:
            print(f"Post ID: {post['id']}")
            print(f"Title: {post['title']}")
     

def view_all_users() -> None:
        url = "https://jsonplaceholder.typicode.com/users"
        data = get_json_data(url)
        if data is None:
            print("No Data found!")
        else:
            for user in data:
                print(f"User ID: {user['id']} -- Name : {user['name']}")
    

def get_json_data(url: str, params: dict | None = None, timeout: int = 10)-> dict | list[dict] | None:
    try:
        response = requests.get(url, params=params, timeout=timeout)
        response.raise_for_status()
    except requests.exceptions.RequestException as error:
        print(f"Request failed: {error}")
    else:
        try:
            data = response.json()
        except requests.exceptions.JSONDecodeError as error:
            print(f"Data failed to parse: {error}")
        else:
            return data


def main() -> None:
    while True:
        options = {
            1: "View user information",
            2: "View posts by user",
            3: "View all users",
            4: "Exit"
        }
        for key, value in options.items():
            print(f"{key}. {value}")
        option = input("Option: ")
        if option == "1":
            view_user()
        elif option == "2":
            view_posts()
        elif option == "3":
            view_all_users()
        elif option == "4":
            break
        else:
            print("Invalid option!")


if __name__ == "__main__":
    main()
