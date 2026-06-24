from sklearn.preprocessing import LabelEncoder
import pandas as pd

data = {
    'Name':['Ram','Kamal','Ajay','Neetu','Kavi','Sapu'],
    'Age':[25,None,32,20,21,22],
    'Salary':[5000,6000,None,7000,8000,9000],
    'Gender':['male','male','male',None,'female','female']
}

df = pd.DataFrame(data)
print("Original DataFrame")
# print(df)


df.fillna({'Age': round(df['Age'].mean()) }, inplace=True)
df['Salary'] = df['Salary'].fillna(df['Salary'].mean())
print(df)


le = LabelEncoder()
df_label = df.copy()
df_label['Gender'] = df_label['Gender'].fillna('unknown')
df_label['Gender_Encoded'] = le.fit_transform(df_label['Gender'])
#  f -> 0     U -> 0
#  m -> 1     f -> 1
#  u -> 2     m -> 2
print("DataFrame after Label Encoding is:")
print(df_label)


# 2. One Hot Encoding

data = {
    "Color": ["Red", "Blue", "Green", "Red", "blue"],
}

df = pd.DataFrame(data)
# print("Original DataFrame")
# print(df)

# Fix casing first
df['Color'] = df['Color'].str.lower()

encoded_df = pd.get_dummies(df , columns = ['Color'] , prefix= 'Fav_Color')
print("\nDataFrame after One-Hot Encoding")
print(encoded_df)




from sklearn.preprocessing import LabelEncoder
import pandas as pd
import numpy as np

data = { 'Color':[ 'red' , 'green' , 'blue' , 'orange' , 'green' , 'blue' , np.nan]}
df = pd.DataFrame(data)
# print(df)


# 1. Handle Missing Value
df.dropna(inplace = True) 
print(df)

# Method - 1
le = LabelEncoder()
df["color_encoded_1"] = le.fit_transform(df['Color'])
print(df)

# Method - 2
df["color_encoded_2"] = LabelEncoder().fit_transform(df['Color'])
print(df)

# Method - 3
import sklearn
df["color_encoded_3"] = sklearn.preprocessing.LabelEncoder().fit_transform(df['Color'])
print(df)



# 2. One Hot Encding:-
from sklearn.preprocessing import OneHotEncoder
df.drop(columns = {"color_encoded_1" , "color_encoded_2" , "color_encoded_3"} , inplace = True)
print(df)

#Method - 1
# df_encoded = pd.get_dummies(df , columns = ['Color'])
# df_encoded = pd.get_dummies(df , columns = ['Color'] , dtype = int)
# print(df_encoded)


# Method - 2
encoder = OneHotEncoder(sparse_output=False)

encoded = encoder.fit_transform(df[['Color']])
encoded_df = pd.DataFrame(
    encoded,
    columns=encoder.get_feature_names_out(['Color'])
)
print(encoded_df)




import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

data = {
    "age": [10, 20, np.nan, 26, 30],
    "gender": ["male", "female", "others", "male", None],
    "name": ["dheeraj", "kavi", "sapu", "yash", "hello"]
}


df = pd .DataFrame(data)
print("Original DataFrame")
print(df)

df['age'] = df['age'].fillna(round(df['age'].mean()))
df['gender'] = df['gender'].fillna('unknown')
print(df)


# 1. Label Encoding
le = LabelEncoder()
df['gender_encoded'] = le.fit_transform(df['gender'])
print("DataFrame after Label Encoding: ")
print(df)

# 2. One Hot Encoding
# df_encoded = pd.get_dummies(df , columns = ['gender'] , dtype = int)
# print("DataFrame after One Hot Encoding is:")
# print(df_encoded)

oneHot = OneHotEncoder(sparse_output = False)
encoded = oneHot.fit_transform(df[['gender']])
# print(encoded.toarray())
df_encoded = pd.DataFrame(encoded , columns = oneHot.get_feature_names_out(["gender"]))
df_final = pd.concat([df , df_encoded] , axis = 1)
print(df_final)







