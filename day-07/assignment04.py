def completion_rate(developer):
    if not developer['projects']:
        return 0
    completed = 0
    total = 0
    for project in developer['projects']:
        total += 1
        if project['completed']:
            completed += 1
    rate = completed/total * 100
    return rate

def rank_developers(developers):
    return sorted(developers, key=lambda developer:completion_rate(developer), reverse=True)


developers = [
    {
        "name": "Alex",
        "projects": [
            {"name": "Task Manager", "language": "Python", "completed": True},
            {"name": "Website", "language": "HTML", "completed": False}
        ]
    },
    {
        "name": "Jordan",
        "projects": [
            {"name": "API", "language": "Python", "completed": True},
            {"name": "Game", "language": "C", "completed": True}
        ]
    },
    {
        "name": "Taylor",
        "projects": [
            {"name": "Portfolio", "language": "JavaScript", "completed": False}
        ]
    }
]

for developer in rank_developers(developers):
    print(developer['name'])