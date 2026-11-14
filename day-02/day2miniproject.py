def analyze_people(people):
    total= len(people)
    adults = []
    oldest_age = people[0]["age"]
    youngest_age = people[0]["age"]
    name_of_oldest = people[0]["name"]
    name_of_youngest = people[0]["name"]
    sum_= sum(item["age"] for item in people)
    average_age = sum_/len(people)

    for person in people:
        if person["age"] > oldest_age:
            oldest_age = person["age"]
            name_of_oldest = person["name"]
        if person["age"] < youngest_age:
            youngest_age = person["age"]
            name_of_youngest = person["name"]
        if person["age"] >= 30:
                adults.append(person["name"])

    result = {
        "total": total,
        "adults": adults,
        "oldest": name_of_oldest,
        "youngest": name_of_youngest,
        "average_age": average_age 
    }
    return result


people = [
    {"name": "Alice", "age": 25},
    {"name": "Bob","age": 31},
    {"name": "Charlie", "age": 22},
    {"name": "Diana", "age": 35},
    {"name": "Ethan", "age": 28}
]

message = analyze_people(people).values()

for value in message:
    print(value)