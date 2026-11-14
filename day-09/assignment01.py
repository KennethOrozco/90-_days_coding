def task_summary(developers):
    summary = {}
    for developer in developers:
        name = developer['name']
        if name not in summary:
            summary[name] = {"total_tasks": 0, "completed_tasks": 0}
        for project in developer['projects']:
            for task in project['tasks']:
                summary[name]['total_tasks'] += 1
                if task['completed']:
                    summary[name]['completed_tasks'] += 1
    return summary




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

print(task_summary(developers))