import pandas as pd

df = pd.read_csv('students.csv')

print(df.describe())
print(df.groupby("Name")["Age"].mean())

df.rename(columns={"Marks ": "Score"}, inplace=True)
df.rename(columns={"Phone": "Mobile NUMBER"}, inplace=True)

df["Score"] = df["Score"].astype(int)
print(df)