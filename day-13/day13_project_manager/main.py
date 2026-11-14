from project_manager import Developer

developer = Developer("Alex")


while True:
    options = {
        1: "View Projects",
        2: "Add Project",
        3: "Add Task",
        4: "Complete Task",
        5: "View Project Completion Rates",
        6: "View Overall Completion Rate",
        7: "Exit"
    }
    for key, value in options.items():
        print(f"{key}. {value}")
    option = input("Option: ")
    if option == "1":
        for project in developer.projects:
            print(project.name)
    elif option == "2":
        name = input("Project Name: ")
        try:
            developer.add_project(name)
        except ValueError as error:
            print(error)
        else: print("Project was added!")
    elif option == "3":
        name = input("Project Name: ")
        title = input("Task Title: ")
        found = developer.find_project(name)
        if found is None:
            print("Project not found!")
        else:
            task = found.find_task(title)
            if task is not None:
                print("Task already exist!")
            else:
                found.add_task(title)
                print("Task was added!")
    elif option == "4":
        for project in developer.projects:
            for task in project.tasks:
                status = "Completed" if task.completed else "Incomplete"
                print(f"Project: {project.name} -- Task: {task.title} -- Status: {status}")
        name = input("Project Name: ")
        title = input("Task Title: ")
        found = developer.find_project(name)
        if found is None:
            print("Project not found!")
        else:
            try:
                found.complete_task(title)
            except ValueError as error:
                print(error)
            else:
                print("Task status has been changed to Completed!")
    elif option == "5":
        for project in developer.projects:
            print(f"Project: {project.name} -- Completion Rate: {project.completion_rate()}%")
    elif option == "6":
        print(f"Overall completion rate: {developer.overall_completion_rate()}%")
    elif option == "7":
        break
    else:
        print("Invalid option!")
        
