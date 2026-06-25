# Feature Scale:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

data = {
    'Experience' : [300 , 600 , 900 , 1500],
    'Salary': [1000 , 1500 , 2000 , 3000]
}
df = pd.DataFrame(data)
print(df)

# Standard Scaler
scaler = StandardScaler()
df['Experience'] = scaler.fit_transform(df[['Experience']])
print(df)

# Split Data
x = df['Experience']
y = df['Salary']
print(x)
print(y)


plt.plot(x , y , marker = 'o'  )
plt.title("Experience VS Salary")
plt.xlabel('Experience')
plt.ylabel('Salary')
plt.show()

# Data Split using Traning Testing
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split


data = {
    "experience":[300,600,900,1500],
    "salary":[1000,1500,2000,3000]
}
 
df = pd.DataFrame(data)
print(df)
 
# split data
x = df['experience'] # capital X
y = df['salary']
 
# train test split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2)
print("x train: ",x_train)
print("x test: ",x_test)
print("y train: ", y_train)
print("y test: ", y_test)



# data split training testing
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
 
data = "https://raw.githubusercontent.com/rajendra0968jangid/Ds-Arya/main/extended_salary_data.csv"
 
df = pd.read_csv(data)
# print(df)
 
# split data
x = df['experience'] # capital X
y = df['salary']
 
# train test split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)
print("x train: ",x_train )
print("x test: ",x_test)
print("y train: ", y_train)
print("y test: ", y_test)



from sklearn.linear_model import LinearRegression
import pandas as pd

# Model fit
model = LinearRegression()
model.fit(x_train, y_train)

# Input from user
user = int(input("Enter your Experience: "))

# Create DataFrame for prediction
df1 = pd.DataFrame({
    "experience": [user]
})

print(df1)

# Prediction
pred_data = model.predict(df1)

print("Predicted Salary:", pred_data[0])


