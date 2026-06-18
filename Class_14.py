# import pandas
# df = pd.Series([10,20,30])
# print(df)

import pandas as pd

dict = {"Name":["Zoro","Luffy","Nami","Sanji","Ussop"],
        "Age":[20,21,22,23,24],
        "Salary":[{"In-Hand":"15000","ctc":"1.21lpa"},{"In-Hand":"25000","ctc":"2.21lpa"},
                  {"In-Hand":"89000","ctc":"11.21lpa"},{"In-Hand":"50000","ctc":"4.21lpa"},
                  {"In-Hand":"35000","ctc":"4.21lpa"}]
                }

df = pd.DataFrame(dict)
print(df)


# 1. Save data into a csv file
df.to_csv("Save_CSV.csv") 
# If we dont want index in code then set index = False
# df.to_csv("Save_Output.csv", index=False) 

# 2. Save data into a excel file
df.to_excel("Save_EXCEL.xlsx") 

# 3. Save data into a csv file
df.to_json("Save_JSON.json") 


""" CSV -->  Comma Separated Values.
    JSON --> Javascript object notation
"""