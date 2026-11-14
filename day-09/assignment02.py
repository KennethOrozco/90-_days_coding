def project_index(developers):
    index = {}
    for developer in developers:
        for project in developer['projects']:
            name = project['name']
            index[name] = {"developer": developer['name'], "team": developer['team'], "language": project['language']}
    return index


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

print(project_index(developers))