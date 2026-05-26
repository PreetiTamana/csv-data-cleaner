import pandas as pd
df = pd.read_csv("sample.csv")
print(df)

## print first 5 rows

print(df.head())

# detect missing values

print(df.isnull().sum())

#fill all the missing age with average age and salary

df["Age"] = df["Age"].fillna(df["Age"].mean()).astype(int)

df["Salary"] = df["Salary"].fillna(df["Salary"].mean())

print(df)

## remove duplicate rows

df = df.drop_duplicates()

print("\nCleaned Data:")
print(df)

## generate statistics
print("\nSummary Statistics:")
print(df.describe())

##save

df.to_csv("cleaned_data.csv", index=False)
print("\nCleaned CSV saved successfully!")