def get_score(student):
    return student['score']

students = [
    {"name": "Alex", "score": 82},
    {"name": "Jordan", "score": 95},
    {"name": "Taylor", "score": 76},
    {"name": "Morgan", "score": 88}
]

score_high = sorted(students, key=get_score, reverse=True)

for student in score_high:
    print(f"{student['name']}: {student['score']}")

