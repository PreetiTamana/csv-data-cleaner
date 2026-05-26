import pandas as pd

file = input("Enter CSV file name (default sample.csv): ") or "sample.csv"
df = pd.read_csv(file)
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


## filtering rows
choice = input("Filter by age? (y/n): ")

if choice.lower() == "y":
    min_age = int(input("Enter minimum age: "))
    df = df[df["Age"] >= min_age]

## generate statistics
print("\nSummary Statistics:")
print(df.describe())

##save

df.to_csv("cleaned_data.csv", index=False)
print("\nCleaned CSV saved successfully!")