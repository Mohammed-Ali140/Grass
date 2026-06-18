import pandas as pd

df = pd.read_json("student-data2.json")
print(df)


# df.sort_values("english" , inplace = True) # ByDefault Ascending
df.sort_values(by=["english"], inplace = True)
print(df)


df.sort_values("english",ascending = False , inplace = True) # Descending
print(df)

df.sort_values(by=["english","maths"],ascending = [False,True] , inplace = True) # Descending
print(df)

df['name'] = df['name'].str.lower()
df.sort_values(by=["name"], inplace = True)
print(df)


# add column 
df['Total'] = df["physics"] + df["maths"] + df["english"]
print(df)

# add row
df.loc[14] = ["luffy","Male",56,67,78,201]
print(df)

# delete column and row
# 1. delete column
df.drop("totol",axis = 1)
# 2, delete row
df.drop("totol",axis = 0)



url = "https://raw.githubusercontent.com/rajendra0968jangid/Ds-Arya/main/file2.json"
df = pd.read_json(url)
df['doj'] = ['2025-01-10','2025-02-10','2025-03-10','2025-04-10','2025-05-10']
df['doj'].dtype
 
# convert string to date
df['doj'] = pd.to_datetime(df['doj'])
df['doj'].dtype
# date operation
df['doj'].dt.year
df['doj'].dt.month
df['doj'].dt.day
df['doj'].dt.day_name()
 
# 20 days
df['doj'] + pd.to_timedelta(20,unit='D')
df['doj'] + pd.to_timedelta('20 days')



l = {
    "ID": [101, 102, 103, 104, 105, 106],
    "Name": ["Amit", "Riya", None, "Sara", "John", "Neha"],
    "Department": [None, "HR", "Finance", "IT", "Sales", "HR"],
    "Salary": [50000, 45000, 600000, 55000, None, 152000],
    "Experience": [2, 3, None, 3, 1, 4]
}

df = pd.DataFrame(data = l)
print(df)
print(df.isnull())

url = "https://raw.githubusercontent.com/rajendra0968jangid/Ds-Arya/main/file2.json"
df = pd.read_json(url)
print(df)
print(df.isnull())

# df.loc[4, "marks"] = pd.NA
# df.loc[4, "marks"] = None
# df.loc[2, "roll no"] = None

# Tells count of null value in each columns
print(df.isnull().sum())   

# Gives total null value in DataFrame
print(df.isnull().sum().sum())

""" Removing columns and rows with missing values
       Syntax:-    df.dropna(axis = 0, inplace = True)   --> Remove row
       Syntax:-    df.dropna(axis = 1, inplace = True)   --> Remove column
"""

df.dropna(axis = 1 , inplace = True)   # Drop Columns containing null\NaN
print(df)

df.dropna(axis = 0 , inplace = True)   # Drop rows containing null\NaN
print(df)

# Replaces all null/NaN valye with 0
print(df.fillna(0 , inplace = True))

# REplacing null/NaN values with some calculated value
# Fill NaN values in a column with its mean
df["roll no"] = df["roll no"].fillna(df["roll no"].mean())
print(df)

df["marks"] = df["marks"].fillna(df["marks"].mean())
print(df)
