def developer_performance(developers):
    summary = {}
    for developer in developers:
        name = developer['name']
        summary[developer['name']] = {"projects": 0, "completed_projects": 0, "tasks": 0, "completed_tasks": 0, "task_completion_rate": 0}
        for project in developer['projects']:
            summary[name]['projects'] += 1
            if project['completed']:
                summary[name]['completed_projects'] += 1
            for task in project['tasks']:
                summary[name]['tasks'] += 1
                if task['completed']:
                    summary[name]['completed_tasks'] += 1
        if summary[name]['tasks'] > 0:
            summary[name]['task_completion_rate'] = summary[name]['completed_tasks']/ summary[name]['tasks'] * 100
        else:
            summary[name]['task_completion_rate'] = 0
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




print(developer_performance(developers))