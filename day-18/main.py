import pandas as pd


students = [
    {"name": "Alice", "age": 20, "score": 85},
    {"name": "Bob", "age": 22, "score": 92},
    {"name": "Charlie", "age": 19, "score": 78},
    {"name": "David", "age": 21, "score": 95},
    {"name": "Eve", "age": 23, "score": 88},
    {"name": "Frank", "age": 20, "score": 73}
]

df = pd.DataFrame(students)


average_score = df['score'].mean()

print(f"Average score: {average_score:.2f}")

print(df['score'].max())

print(df["score"].min())

average_age = df['age'].mean()

print(f"Average age: {average_age:.2f}")

score_count = df['score'].count()

print(f"Number of scores: {score_count}")

print(df['score'].describe())


