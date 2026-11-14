def language_summary(developers):
    languages = {}

    for developer in developers:
        for project in developer["projects"]:
            language = project["language"]

            if language not in languages:
                languages[language] = {
                    "projects": 0,
                    "completed": 0
                }

            languages[language]["projects"] += 1

            if project["completed"]:
                languages[language]["completed"] += 1

    return languages

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

print(language_summary(developers))
