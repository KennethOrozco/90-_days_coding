def has_incomplete_tasks(developer):
    return any(not task['completed'] for project in developer['projects'] for task in project['tasks'])


def all_tasks_completed(project):
    if project['tasks'] and all(task['completed'] for task in project['tasks']):
        return True
    return False

developers = [
    {
        "name": "Alex",
        "team": "Backend",
        "projects": [
            {
                "name": "API",
                "language": "Python",
                "completed": True,
                "tasks": [
                    {"name": "Authentication", "completed": True},
                    {"name": "Database", "completed": True},
                    {"name": "Testing", "completed": False}
                ]
            },
            {
                "name": "Worker",
                "language": "Python",
                "completed": False,
                "tasks": [
                    {"name": "Queue", "completed": True},
                    {"name": "Retries", "completed": False}
                ]
            }
        ]
    },
    {
        "name": "Jordan",
        "team": "Frontend",
        "projects": [
            {
                "name": "Dashboard",
                "language": "JavaScript",
                "completed": True,
                "tasks": [
                    {"name": "Layout", "completed": True},
                    {"name": "Charts", "completed": True}
                ]
            }
        ]
    },
    {
        "name": "Taylor",
        "team": "Backend",
        "projects": []
    }
]

for developer in developers:
    print(has_incomplete_tasks(developer))

for developer in developers:
    for project in developer['projects']:
        print(all_tasks_completed(project))