def average_score(students):
    if not isinstance(students, list):
        raise TypeError("Students must be a list")
    if not students:
        return 0
    score = 0
    for student in students:
        if not isinstance(student, dict):
            raise TypeError("Each student must be a dictionary")

        if "score" not in student:
            raise ValueError("Student is missing score")

        if not isinstance(student['score'], (int, float)):
            raise TypeError("Score must be numeric")
        
        score += student["score"]
    
    return score / len(students)
        


students = [
    {"name": "Alex", "score": 92},
    {"name": "Jordan", "score": 85},
    {"name": "Taylor", "score": 78}
]

print(average_score(students))