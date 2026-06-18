import pandas as pd

l = {
    "Emp_ID": [101, 102, 103, 104, 105, 106],
    "Name": ["Amit", "Riya", "Raj", "Sara", "John", "Neha"],
    "Department": ["IT", "HR", "Finance", "IT", "Sales", "HR"],
    "Salary": [50000, 45000, 600000, 55000, 52000, 152000],
    "Experience": [2, 3, 5, 3, 1, 4],
    "Performance Score": [85,90,95,80,98,79]

}

df = pd.DataFrame(data = l)
print("Sample DataFrame:")
print(df)

# Selecting single Column -> Returns series
print(df["Name"])

# Selecting Multiple Column -> Returns DataFrame
subset = df[["Name" , "Salary"]]
print(subset)



# 2. Filtering Rows

high_Salary = df[df["Salary"] > 50000]
print("Employee with Salary Greather than 50000:")
print(high_Salary)

# Employee wuth Experience above 2 years and salary above 50000
# data = df[(df["Experience"] > 2) & (df["Salary"] > 50000)]
data = df.loc[(df["Experience"] > 2) & (df["Salary"] > 50000)]
print(data)

# Using OR Condition 
data = df[(df["Experience"] > 2) | (df["Salary"] > 50000)]
print(data)



import pandas as pd

l = {
    "ID": [101, 102, 103, 104, 105, 106],
    "Name": ["Amit", "Riya", "Raj", "Sara", "John", "Neha"],
    "Department": ["IT", "HR", "Finance", "IT", "Sales", "HR"],
    "Salary": [50000, 45000, 600000, 55000, 52000, 152000],
    "Experience": [2, 3, 5, 3, 1, 4]
}

df = pd.DataFrame(data = l)


""" 1. rename() --> is used to change the names of columns or index labels  """

# a) rename Single column
# df.rename(columns= {"Name":"Emp_Name"} , inplace = True)
# print(df)

# b) Rename multiple columns : - df.rename(columns = {"old_name": "new_name"} , inplace=True)
df.rename(columns= {"Name":"Emp_Name" ,  "ID":"Emp_ID"},inplace = True)
# print(df)

# 3. Rename row indices :- df.rename( index = {old_index: new_index} ,  inplace=True)
# df.rename(index = {0 : "A" ,1 : "B" ,2 : "C" ,3 : "D" ,4 : "E" ,5 : "F" } , inplace= True)
# print(df)

# Convert all column names to Uppercase and  lowercase:
# df.rename(columns=str.upper)
# df.rename(columns=str.lower)


""" 2. Adding Coloumn:-  """

# a) df["Column_Name"] =   some_data   
df["Bonus"] = df["Salary"] * 0.1
# print(df)

# b) using insert method
# Syntax:-  df.insert(loc , "Column_Namre" , Values)

df.insert(4 , "Performance Score" , [79,90,95,80,85,87])
# print(df)



""" 3. Updating Data   """

#.loc[]    --> df.loc[row_index , "Column_Name"] = new_values
df.loc[1 , "Salary"] = 80000   # Specific Column Update
# print(df)


# Updating Multiple Value at a time
df["Salary"] = df["Salary"] * 1.05   # All Column Update
# print(df)

# df.drop(columns = ["Performance Score"] , inplace = True)
# df.drop("Performance Score", axis = 1 , inplace = True)
df.drop(["Performance Score" , "Bonus"], axis = 1 , inplace = True)
# print(df)

# df.drop(2 , inplace = True)
# df.drop(2 , axis = 0 , inplace = True)
# df.drop([2 , 5] , axis = 0, inplace = True)
# print(df)

"""   loc[] is used to select rows and columns by their labels (names). 
           syntax:-   df.loc[row_label, column_label]
"""
#loc[]
print(df.loc[3])                                            # Get a single row
print(df.loc[3 , "Salary"])                                 # Get a single value
print(df.loc[[1,3]])                                        # Get multiple rows
print(df.loc[[1 , 3] , ["Emp_Name" , "Experience"]])        # Get specific rows and columns
print(df.loc[0:2])         # Get a rnge of rows  --> In loc, the ending index is included.
print(df.loc[df["Salary"] > 50000])                         # Filter rows using a condition
print(df.loc[:, "Emp_Name"])                                # Single column (Series)
print(df.loc[:, ["Emp_Name" , "Salary"]])                   # Single column (DataFrame)
df.loc[1, "Experience"] = 4                                 # Modify data using loc
print(df)
            

# iloc[]            
print(df.iloc[1]) # Get a single row
print(df.iloc[1, 1]) # Get a sinle value
print(df.iloc[[1 , 3]]) # Get multiple rows
print(df.iloc[[0, 2], [0, 2]]) # Get specific rows and columns
print(df.iloc[0:2])    # Slicing -> In iloc[], the ending index is excluded.
print(df.iloc[: , 1])   # Get a specific Column
print(df.iloc[: , [0 , 3]]) # Get multiple columns
print(df.iloc[df["Salary"] > 50000  , 1])  
print(df.iloc[df["Salary"] > 50000 ])