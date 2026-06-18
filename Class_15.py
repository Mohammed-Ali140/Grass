import pandas as pd

data = {
    "Name":["Luffy","Zoro","Sanji"],
    "Age":[20,22,21],
    "City":["East_Blue","West_Blue","North_Blue"]
}

df = pd.read_json("student-data2.json")

# print(f"Display First 7 rows of file {df.head(7)}")  # head(n)
print(df.head())  # ByDefault display first 5 rows

# print(f"Display last 7 rows of file {df.tail(7)}")   # tail(n)
print(df.tail())  # ByDefault display last 5 rows


import pandas as pd 
data = {
    "Emp_ID": [101, 102, 103, 104, 105, 106],
    "Name": ["Amit", "Riya", "Raj", "Sara", "John", "Neha"],
    "Department": ["IT", "HR", "Finance", "IT", "Sales", "HR"],
    "Salary": [50000, 45000, 60000, 55000, 48000, 52000],
    "Experience": [2, 3, 5, 4, 1, 3]
}

DF1=pd.DataFrame(data)
print(DF1)

# 1. head()
print("head ")
print(DF1.head())    # Returns first 5 rows
print("\n")
print(DF1.head(6))   # Returns first 6 rows
print("\n")
print(DF1.head(-3))  # Returns all rows except the last 3 rows.

# tail()
print("\n tail")
print(DF1.tail())    # Returns the last 5 rows (default).
print("\n")
print(DF1.tail(3))   # Returns the last 3 rows
print("\n")
print(DF1.tail(-4))  # Returns all rows except the first 4 rows

  
# df.info()
# print(df.info())   # It will as above but also gives None in last
df = pd.DataFrame(data)
df.info()



data1 = {
    "Emp_ID": [101, 102, 103, 104, 105, 106],
    "Name": ["Amit", "Riya", "Raj", "Sara", "John", "Neha"],
    "Salary": [50000, 45000, 60000, 55000, 48000, 52000],
    "Experience": [2, 3, 5, 4, 1, 3]
}
df1 = pd.DataFrame(data1)
print(df1.describe())


print("Shape:", df1.shape)  #Returns the number of rows and columns as a tuple
# print(df1.shape[0])  # Rows
# print(df1.shape[1])  # Columns

print("Columns:", df1.columns)    # Returns the names of all columns
# print("Columns:", df1.columns.tolist())  # To get them as a Python list
