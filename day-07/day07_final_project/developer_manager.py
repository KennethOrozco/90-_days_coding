import json

def load_developers(file_path):
    try:
        with open(file_path, "r") as file:
            content = json.load(file)
            return content
    except FileNotFoundError:
        print("File not found!")
        return []

def save_developers(developers, file_path):
    with open(file_path, "w") as file:
        json.dump(developers, file)

def find_developer(developers, name):
    for developer in developers:
        if name.lower() == developer['name'].lower():
            return developer
    return None

def add_developer(developers, name):
    info = {
        "name": name,
        "projects": []
    }
    for developer in developers:
        if info['name'].lower() == developer['name'].lower():
            return False
    developers.append(info)
    return True

def add_project(developers, developer_name, project_name, language):
    project = {"name": project_name, "language": language, "completed": False}
    for developer in developers:
        if developer_name.lower() == developer['name'].lower():
            developer['projects'].append(project)
            return True
    return False   
def complete_project(developers, developer_name, project_name):
    for developer in developers:
        if developer_name.lower() == developer['name'].lower():
            for project in developer['projects']:
                if project_name.lower() == project['name'].lower():
                    project['completed'] = True
                    return True
    return False

def completion_rate(developer):
    if not developer['projects']:
        return 0
    total = 0
    completed = 0
    for project in developer['projects']:
        total += 1
        if project['completed']:
            completed += 1
    return completed/total * 100

def rank_developers(developers):
    return sorted(developers, key=lambda developer:completion_rate(developer), reverse=True)

def language_summary(developers):
    languages = {}
    for developer in developers:
        for project in developer['projects']:
            language = project['language']
            if language not in languages:
                languages[language] = {"projects": 0, "completed": 0}

            languages[language]["projects"] += 1

            if project['completed']:
                languages[language]['completed'] += 1
    return languages
    
            


           

        