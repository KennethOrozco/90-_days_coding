import pandas as pd

def missing_fields(df: pd.DataFrame) -> pd.Series:
    return df.isna().sum()

def calculate_average(df: pd.DataFrame) -> float:
    return df['score'].mean()

def highest_score(df: pd.DataFrame) -> float:
    return df['score'].max()

def lowest_score(df: pd.DataFrame) -> float:
    return df['score'].min()

students = [
    {"name": "Alice", "age": 20, "score": 85},
    {"name": "Bob", "age": 22, "score": 92},
    {"name": "Charlie", "age": 19, "score": None},
    {"name": "David", "age": 21, "score": 95},
    {"name": "Eve", "age": None, "score": 88},
    {"name": "Frank", "age": 20, "score": 73},
    {"name": None, "age": 24, "score": 81},
    {"name": "Grace", "age": 23, "score": None}
]

df = pd.DataFrame(students)

cleaned_df = df.fillna({"name": "Unknown", "age": 0,})

print(df)

print(missing_fields(df))

print(cleaned_df)

print(f"Average: {calculate_average(df):.2f}")

print(f"Highest score: {highest_score(df)}")

print(f"Lowest score: {lowest_score(df)}")

print(df[df['score'] >= 85])

print(df[["name", "score"]][df["score"] >= 90])

print(df['score'].describe())

