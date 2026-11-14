import json

def load_students(file_path):
    try:
        with open(file_path, "r") as file:
            content = json.load(file)
            return content
    except FileNotFoundError:
        print("File not found!")
        return []

def save_students(students, file_path):
     with open(file_path, "w") as file:
        json.dump(students, file)

def student_averages(students):
    averages = {}
    for student in students:
        if student['scores']:
            average = sum(student['scores'])/len(student['scores'])
            averages[student['name']]= average
        else:
            averages[student['name']] = 0
    return averages

def top_student(students):
    if not students:
        return
    averages = student_averages(students)
    top_average = 0
    student_name = None
    for student, average in averages.items():
        if average > top_average:
            top_average = average
            student_name = student
    return student_name

def students_above_average(students):
    if not students:
        return []
    averages = student_averages(students)
    averages_all = sum(averages.values())/len(averages)
    above_average = [student for student, average in averages.items() if  average > averages_all]
    return above_average

def add_student(students, name, scores):
    add = {
        "name": name,
        "scores":scores
    }
    students.append(add)

def add_score(students, name, score):
    for student in students:
        if student['name'] == name:
            student['scores'].append(score)
            return True
    return False
        


