def total_completed_projects(users):
    sum_ = 0
    for user in users:
        sum_ += user['projects']['completed']
    return sum_
            




users = [
    {
        "name": "Alex",
        "age": 24,
        "skills": ["Python","HTML"],
        "projects": {
            "completed": 3,
            "active": 2
        }
    },
    {
        "name": "Jordan",
        "age": 31,
        "skills": ["Python", "JavaScript", "SQL"],
        "projects": {
            "completed": 7,
            "active": 3
        }
    },
    {
        "name": "Taylor",
        "age": 27,
        "skills": ["HTML", "CSS"],
        "projects": {
            "completed": 4,
            "active": 3
        }
    }   
]

for user in users:
    print(f"{user['name']}")
    for skill in user['skills']:
        print(f"{skill}")
    print()


print(users[1]["projects"]["completed"])

python_users = [user['name'] for user in users if "Python" in user['skills']]

print(python_users)

print (total_completed_projects(users))