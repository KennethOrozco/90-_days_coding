import json

def load_courses(file_path):
    try:
        with open(file_path, "r") as file:
            content = json.load(file)
            return content
    except FileNotFoundError:
        return []

def save_courses(courses, file_path):
    with open(file_path, "w") as file:
        json.dump(courses, file)

def course_statistics(courses):
    statistics = {}
    for course in courses:
        name = course['name']
        total = 0
        statistics[name] = {"students": 0, "completed": 0, "average_score": 0}
        for student in course['students']:
            statistics[name]['students'] += 1
            total += student['score']
            if student['completed']:
                statistics[name]['completed'] += 1
            
        if statistics[name]['students'] > 0:
            statistics[name]['average_score'] = total / statistics[name]['students']
        else:
            statistics[name]['average_score'] = 0
    return statistics

def find_courses(courses, category=None, has_students=None):
    filtered = []
    for course in courses:
        matches = True

        if category is not None and category.lower() != course['category'].lower():
            matches = False

        if has_students is not None and has_students != bool(course['students']):
            matches = False
            
        if matches:
                filtered.append(course)
    return filtered

def top_students(courses):
    if not any(course['students'] for course in courses):
        return []
    highest = max(student['score'] for course in courses for student in course['students'])
    return [student['name'] for course in courses for student in course['students'] if student['score'] == highest]

def rank_courses(courses):
    statistics = course_statistics(courses)
    return sorted(courses, key=lambda course:(statistics[course['name']]['average_score'], statistics[course['name']]['students']), reverse=True)

def add_student(courses, course_name, student):
    for course in courses:
        if course_name.lower() == course['name'].lower():
            course['students'].append(student)
            return True
    return False




