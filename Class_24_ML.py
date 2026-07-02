# Decision tree
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier 
from sklearn.metrics import mean_absolute_error


# data set
data = {
    "age":[20,22,25,28,30,35,40,45,50,55],
    "salary":[20000,25000,27000,32000,45000,50000,60000,70000,80000,9000],
    "buy":[0,0,0,0,1,1,1,1,1,0]
}
 
df = pd.DataFrame(data)
print(df)

X = df[['age' , 'salary']]
y = df['buy']

X_train,X_test,y_train,y_test = train_test_split(X , y , test_size = 0.2 , random_state = 42)


# Model
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train , y_train)

# Prediction - 1
new_data = pd.DataFrame({
    'age' : [60],
    'salary' : [75000]
})
predicted_Data = model.predict(new_data)
print(predicted_Data[0])


# print(f"Actual Data: {X_test}")
# # Prediction - 2
# y_pred = model.predict(X_test)
# print(f"Predicted Data : {y_pred}")



# Random Forest - Combination of Multiple Decision Tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


data = {
    "age":[20,22,25,28,30,35,40,45,50,55],
    "salary":[20000,25000,27000,32000,45000,50000,60000,70000,80000,9000],
    "buy":[0,0,0,0,1,1,1,1,1,0]
}

df = pd.DataFrame(data)


X = df[['age' , 'salary']]
y = df['buy']

X_train,X_test,y_train,y_test = train_test_split(X , y , test_size = 0.2 , random_state = 42, stratify=y)

# Model 
model = RandomForestClassifier(random_state= 42 , n_estimators= 10)
model.fit(X_train , y_train)

y_pred = model.predict(X_test)
print(f"Predicted Data : {y_pred}")

print(f"Actual Data: {X_test}")

print(f"Accuracy: {accuracy_score(y_test , y_pred)}")


# In Random Forest = Bagging   and   ensemble learning


# 1. Decision Tree Example
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


data = {
    "Study_Hours": [1,2,3,4,5,6,7,8,2,3,4,5,6,7,8,1,2,5,6,4],

    "Attendance": ["Low","Low","Medium","Medium","High","High","High","High","Low","Medium",
                   "Low","Medium","High","Medium","High","Low","Medium","High","Medium","Low"],

    "Result": ["Fail","Fail","Fail","Pass","Pass","Pass","Pass","Pass","Fail","Fail",
               "Fail","Pass","Pass","Pass","Pass","Fail","Fail","Pass","Pass","Pass"]
}

df = pd.DataFrame(data)
print(df)

df.drop_duplicates(inplace = True)
print(df)

df['Attendance'] = df['Attendance'].map({
    'Low': 1,
    'Medium': 2,
    'High': 3
})



X = df[['Study_Hours' , 'Attendance']]
y = df['Result']

X_train,X_test,y_train,y_test = train_test_split(X , y , test_size = 0.2 , random_state = 42 , stratify= y)


model = DecisionTreeClassifier(random_state= 42)
model.fit(X_train , y_train)

# Prediction for new student
new_data = pd.DataFrame({
    'Study_Hours': [7 , 2 , 9 , 4 , 2],
    'Attendance': [2 , 3 , 2 , 1 , 1]
})
predicted_Data = model.predict(new_data)
print("Prediction:", predicted_Data)

# Prediction for test data
y_pred = model.predict(X_test)
print(f"Actual Features : {X_test}")
print(f"Actual Target : {y_test}")
print(f"Prediction : {y_pred}")
print("Accuracy:", accuracy_score(y_test, y_pred)) # Accuracy

# plt.figure(figsize=(10,6))
# plt.plot()


# Confusion Metrics
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

# Create confusion matrix
cm = confusion_matrix(y_test, y_pred)

# Print matrix
print("Confusion Matrix:\n", cm)

# Display graph
disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=['Fail', 'Pass']
)
disp.plot(cmap="Blues", values_format="d")
plt.title("Decision Tree - Confusion Matrix")
plt.show()

# Confusion Metrics
# from sklearn.metrics import confusion_matrix
# actual = [1,0,1,1,0,1,0,0]
# pred = [1,0,1,0,0,1,1,0]
 
# cm = confusion_matrix(actual,pred)
# print(cm)