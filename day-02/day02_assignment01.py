def analyze_people(people):
    oldest = people[0]["age"]
    youngest = people[0]["age"]
    name_of_oldest = people[0]["name"]
    name_of_youngest = people[0]["name"]
    #sum_= 0
    sum_ = sum(item["age"] for item in people)
    average = sum_/len(people)
    for person in people:
        if person["age"] > oldest:
            oldest = person["age"]
            name_of_oldest = person["name"]
        if person["age"] < youngest:
            youngest = person["age"]
            name_of_youngest = person["name"]

    result= { "oldest": name_of_oldest,
              "youngest": name_of_youngest,
              "average": average
              }
   
        


    return result
    



list_of_people = [
          {"name": "Alice", "age": 25},
          {"name": "Bob", "age": 31},
          {"name": "Charlie", "age": 22},
          {"name": "Diana", "age": 28}
        ]

message = analyze_people(list_of_people).values()

for value in message:
    print(value)
