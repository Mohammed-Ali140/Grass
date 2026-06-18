import numpy as np

# Data structure: [restaurant_id, 2021, 2022, 2023, 2024]

sales_data = np.array([
    [1, 15000, 18000, 22000, 25000],  # Paradise Biryani
    [2, 12000, 14000, 16000, 19000],  # Beijing Bites
    [3, 20000, 23000, 26000, 30000],  # Pizza Hub
    [4, 18000, 21000, 24000, 27000],  # Burger Point
    [5, 16000, 18500, 20500, 23000]   # Chai Point
])

print(sales_data)   
print(f"Shape of the array : {np.shape(sales_data)}")
print(f"Number of dimensions : {np.ndim(sales_data)}")
print(f"Total no of elements : {np.size(sales_data)}")

Restaurant_ID = sales_data[: , 0:1]
print(f"Restaurant Id : {Restaurant_ID.flatten()}")

Sales_2021 = sales_data[: , 1:2]
print(f"Sales in 2021 : {Sales_2021.flatten()}")

Sales_2024 = sales_data[: , 4:5]
print(f"Sales in 2024 : {Sales_2024.flatten()}")

# print(f"Maximum Sales Value: {sales_data.max()}")
print(f"Maximum Sales Value: {np.max(sales_data)}")
print(f"Minimum Sales Value: {np.min(sales_data)}")

Total_Sales_2021 = sales_data[: , 1:2]
print(f"Total Sales in 2021 : {Total_Sales_2021.sum()}")

Average_Sales_2024 = sales_data[: , 4:5]
print(f"Average Sales in 2024 : {Average_Sales_2024.mean()}")



# Ques 12 and 13
Total_Sales_Each_Restaurant = sales_data[:, 1:].sum(axis=1)
print("Total Sales of Each Restaurant:", Total_Sales_Each_Restaurant)

Average_Sales_Each_Restaurant = sales_data[:, 1:].mean(axis=1)
print("Average Sales of Each Restaurant:", Average_Sales_Each_Restaurant)
