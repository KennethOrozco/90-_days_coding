def student_averages(students):
    averages = {}
    for student in students:
        average = sum(student['scores'])/len(student['scores'])
        averages[student['name']]= average
    return averages

def top_student(students):
    averages = student_averages(students)
    top_average = 0
    student_name = None
    for student, average in averages.items():
        if average > top_average:
            top_average = average
            student_name = student
    return student_name

def students_above_average(students):
    averages = student_averages(students)
    averages_all = sum(averages.values())/len(averages)
    above_average = [student for student, average in averages.items() if  average > averages_all]
    return above_average







students = [
    {"name": "Alex", "scores": [82, 91, 78]},
    {"name": "Jordan", "scores": [95, 88, 92]},
    {"name": "Taylor", "scores": [76, 81, 79]},
    {"name": "Morgan", "scores": [88, 90, 85]}
]


print(students_above_average(students))