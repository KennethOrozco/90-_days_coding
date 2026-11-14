import pandas as pd

df = pd.read_csv("messy_students.csv")

print(df)
print(df.shape)
print(df.dtypes)
print(df.isna().sum())
print(df.duplicated().sum())

cleaned_df = df.drop_duplicates().copy()

cleaned_df['age'] = pd.to_numeric(cleaned_df['age'], errors="coerce").astype("Int64")
cleaned_df['score'] = pd.to_numeric(cleaned_df['score'], errors="coerce")

print(cleaned_df.isna().sum())
average_score = cleaned_df['score'].mean()
highest = cleaned_df['score'].max()
lowest = cleaned_df['score'].min()
print(f"Average score: {average_score:.2f}")
print(f"Highest score: {highest}")
print(f"Lowest score: {lowest}")

cleaned_df.to_csv("cleaned_students.csv", index =False)
verified_df = pd.read_csv("cleaned_students.csv")
print(verified_df.shape)


