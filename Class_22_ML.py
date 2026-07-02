# Polynomical regression
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
 
df = pd.DataFrame({
    "Experience":[1,2,3,4,5]
})
x = df
y = [10, 20, 50, 90, 150]
 
# poly feature
poly = PolynomialFeatures(degree=2)  # x**2
x_poly = poly.fit_transform(x)
print(x_poly)
 
# model
model = LinearRegression()
model.fit(x_poly,y)
 
# prediction
input_data  = int(input('Enter the experience: '))
new_data = pd.DataFrame({
    "Experience":[input_data]
})
 
# # convert new data to poly
# u_new_data = poly.fit_transform(new_data)
# predicted_data = model.predict(u_new_data)
# print(predicted_data[0])
 
# plt.plot(x_poly,y)
# plt.show()



# Linear reg -> under ifitting
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.DataFrame({
    "label": [1, 2, 3, 4, 5]
})

x = df
y = [10, 20, 50, 90, 150]

# model
model = LinearRegression()
model.fit(x, y)

# predict
input_data = int(input("Enter the label: "))

new_data = pd.DataFrame({
    "label": [input_data]
})

# predicted data
predicted_data = model.predict(new_data)
print(predicted_data[0])



# Over Fitting 
import numpy as np
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

# Dataset
df = pd.DataFrame({
    "label": [1, 2, 3, 4, 5]
})

x = df[["label"]]          # X must be 2D
y = [10, 20, 50, 90, 150]

# Polynomial conversion
poly = PolynomialFeatures(degree=3)
x_poly = poly.fit_transform(x)

# Model
model = LinearRegression()
model.fit(x_poly, y)

# Prediction
input_data = int(input("Enter the label: "))

new_data = pd.DataFrame({
    "label": [input_data]
})

new_poly = poly.transform(new_data)
prediction = model.predict(new_poly)
print("Predicted Value:", prediction[0])




import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

df = pd.DataFrame({
    'Weight' : [120 , 140 , 150 , 170],
    "Size" : [6 , 7 , 7 , 8]
})

x = df
y = ["Apple" , "Apple" , "Orange" , "Orange"]

# Model
model = DecisionTreeClassifier()
model.fit(x,y)

# Prediction Data
# input_weight = int(input("Enter the Weight : "))
# input_size = int(input("Enter the size : "))
# new_data = pd.DataFrame({
#     "Weight": [input_weight],
#     "Size": [input_size]
# })

# Prediction
# predicted_Data = model.predict(new_data)
# print(predicted_Data[0])



import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# Dataset
df = pd.DataFrame({
    "Marks": [20, 40, 41 , 45, 90],
    "Result": ["Fail", "Fail", "Pass" , "Pass", "Pass"]
})

# Features and Target
x = df[["Marks"]]
y = df["Result"]

# Model
model = DecisionTreeClassifier()
model.fit(x, y)

# Prediction
input_Marks = int(input("Enter the Marks: "))

new_data = pd.DataFrame({
    "Marks": [input_Marks]
})

predicted_Data = model.predict(new_data)

print("Predicted Result:", predicted_Data[0])



# Same code as Above But different Approach
# import numpy as np
# import pandas as pd
# from sklearn.tree import DecisionTreeClassifier

# # Dataset
# df = pd.DataFrame({
#     "Marks": [20, 40, 41 , 45, 90]
# })

# # Features and Target
# x = df
# y = ["Fail", "Fail", "Pass" , "Pass", "Pass"]

# # Model
# model = DecisionTreeClassifier()
# model.fit(x, y)

# # Prediction
# input_Marks = int(input("Enter the Marks: "))

# new_data = pd.DataFrame({
#     "Marks": [input_Marks]
# })

# predicted_Data = model.predict(new_data)

# print("Predicted Result:", predicted_Data[0])