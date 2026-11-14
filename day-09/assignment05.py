def find_projects(developers, language=None, completed=None):
    filtered = []
    for developer in developers:
        for project in developer['projects']:
            matches = True

            if language is not None and language.lower() != project['language'].lower():
                 matches = False
            if completed is not None and completed != project['completed']:
                matches = False
            if matches:
                filtered.append(project)
    return filtered
                

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

print(find_projects(developers, language="python", completed=False))