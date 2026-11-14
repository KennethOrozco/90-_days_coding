import developer_manager

file_path = r"C:\Users\koroz\90-days-coding\day-07\day07_final_project\developers.json"

developers = developer_manager.load_developers(file_path)

while True:
    options = {
        1: "View Developers",
        2: "Add Developer",
        3: "Add Project",
        4: "Complete Project",
        5: "View Developer Completion Rates",
        6: "Rank Developers",
        7: "View Language Summary",
        8: "Find Developer",
        9: "Exit"
    }
    for key, value in options.items():
        print(f"{key}. {value}")
    option = input("Choose an option: ")
    if option == "1":
        for developer in developers:
            print(developer['name'])
    elif option == "2":
        while True:
            name = input("What is the name of the Developer you would like to add?: ")
            if name.strip():
                break
            else:
                print("Type a name!")
        developer = developer_manager.add_developer(developers, name)
        if developer:
            developer_manager.save_developers(developers, file_path)
            print("Developer was added!")
        else:
            print("No duplicates allowed!")
    elif option == "3":
        while True:
            developer_name = input("What is the name of the developer you would like to update?: ")
            if developer_name.strip():
                break
            else:
                print("Type a name!")
        while True:
            project_name = input("What is the name of the project?: ")
            if project_name.strip():
                break
            else:
                print("Type a project name!")
        while True:
            language = input("What is it's language?: ")
            if language.strip():
                break
            else:
                print("Type a language!")
        project = developer_manager.add_project(developers, developer_name, project_name, language)
        if project:
            developer_manager.save_developers(developers, file_path)
            print("project was added!")
        else:
            print("project was not added!")
    elif option == "4":
        while True:
            developer_name = input("What is the name of the developer you would like to update?: ")
            if developer_name.strip():
                break
            else:
                print("Type a name!")
        while True:
            project_name = input("What is the project name?: ")
            if project_name.strip():
                break
            else:
                print("Type a project name!")
        complete = developer_manager.complete_project(developers, developer_name, project_name)
        if complete:
            developer_manager.save_developers(developers, file_path)
            print("Project is now marked as complete!")
        else:
            print("Project was not found")
    elif option == "5":
        for developer in developers:
            print(f"{developer['name']}: {developer_manager.completion_rate(developer)}")
    elif option == "6":
        for index, developer in enumerate(developer_manager.rank_developers(developers), start= 1):
            print(f"{index}. {developer['name']}: {developer_manager.completion_rate(developer)}")
    elif option == "7":
        print(developer_manager.language_summary(developers))
    elif option == "8":
        while True:
            name = input("What is the name of the developer you would like to find?: ")
            if name.strip():
                break
            else:
                print("Type a name!")
        developer = developer_manager.find_developer(developers, name)
        if developer:
            print(developer)
        else:
            print("Developer was not found")
    elif option == "9":
        break
    else:
        print("Invalid option!")

