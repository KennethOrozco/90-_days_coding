def get_adults(people):
    adults = []
    for person in people:
        if person["age"]>= 30:
            adults.append(person["name"])

    return adults
        
people = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 31},
    {"name": "Charlie", "age": 22},
    {"name": "Diana", "age":35}
     
]

message = get_adults(people)

print(message)