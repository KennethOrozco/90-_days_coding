def developer_summary(developers):
    summary = {}
    for developer in developers:
        summary[developer['name']]= {"total_projects": 0,"completed_projects": 0}
        for project in developer['projects']:
            summary[developer['name']]["total_projects"] += 1
            if project['completed']:
                summary[developer['name']]['completed_projects'] += 1
    return summary



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

print(developer_summary(developers))