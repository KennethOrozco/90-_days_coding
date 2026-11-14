def create_project(name, language, completed=False):
    return {
        "name": name,
        "language": language,
        "completed": completed
    }

Task_Manager = create_project("Task Manager", "Python", True)

Data_Analyzer =create_project("Data Analyzer", "Python")

Portfolio = create_project(
            language="JavaScript",
            completed=True,
            name="Portfolio"
            )

print(Task_Manager)
print(Data_Analyzer)
print(Portfolio)