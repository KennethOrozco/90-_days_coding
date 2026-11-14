def completed_project_names(developers):
    completed_projects = []

    for developer in developers:
        for project in developer["projects"]:
            if project["completed"]:
                completed_projects.append(project["name"])

    return completed_projects

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