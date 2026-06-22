import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("E-Commerce.csv")
print(df)

print(df.head(5))
print(df.tail(5))
print(f"Total no of rows and columns are: {np.shape(df)}")
print(df.columns)

# print(df.isnull())
print("Missing Vlaue in each column are:")
print(df.isnull().sum())
print(f"Total missing values in Dataset are: {df.isnull().sum().sum()}")

df.dropna(subset = {"City"} , inplace = True)


df["Quantity"] = df["Quantity"].fillna(round(df["Quantity"].mean()))
df["Price"] = df["Price"].fillna(df["Price"].mean())

print(f"Total Quantity sold are: {int(df["Quantity"].sum())}")


df["Total_Sales"] = df["Price"] * df["Quantity"]
print(df)

Total_Revenue = df["Total_Sales"].sum()
print(f"Total Revenue is: {Total_Revenue}")

Avg_Revenue = round(np.mean(df["Total_Sales"]) , 2)
print(f"Average Revenue is: {Avg_Revenue}")


# sales = df["Total_Sales"].to_numpy()
# print("Mean:", np.mean(sales))
# print("Median:", np.median(sales))
# print("Maximum:", np.max(sales))
# print("Minimum:", np.min(sales))
# print("Standard Deviation:", round(np.std(sales), 2))

# avg_sale = np.mean(sales)
# count = np.sum(sales > avg_sale)
# print("Orders greater than average sale:", count)

category_sales = df.groupby("Category")["Total_Sales"].sum()
city_sales = df.groupby("City")["Total_Sales"].sum()
product_sales = df.groupby("Product")["Total_Sales"].sum()


print(df.loc[df["Quantity"] > 2])
print(df.loc[df["Total_Sales"] > 50000])
print(df.loc[df["Category"] == "Electronics"])
delhi_orders = df.loc[df["City"] == "Delhi"]
print(delhi_orders)

df.sort_values(by = "Total_Sales" , inplace = True)
df.sort_values(by = "Price" ,ascending = False , inplace = True)
print(df)




plt.figure(figsize=(16,9))

# Main Title
plt.suptitle("E-Commerce Sales Analysis Dashboard",
             fontsize=18)

# 1. Category Wise Sales
plt.subplot(2,3,1)
plt.bar(category_sales.index, category_sales.values)
plt.title("Category Wise Sales")
plt.xlabel("Category")
plt.ylabel("Revenue")

# 2. City Wise Sales
plt.subplot(2,3,2)
plt.pie(city_sales.values,
        labels=city_sales.index,
        autopct="%1.1f%%")
plt.title("City Wise Sales")

# 3. Product Wise Sales
plt.subplot(2,3,3)
plt.plot(product_sales.index,
         product_sales.values,
         marker="o")
plt.title("Product Wise Sales")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.xticks(rotation=20)
plt.grid()

# 4. Sales Distribution
plt.subplot(2,3,4)
plt.hist(df["Total_Sales"], bins=5)
plt.title("Sales Distribution")
plt.xlabel("Sales")
plt.ylabel("Frequency")

# 5. Product Revenue
plt.subplot(2,3,5)
plt.barh(product_sales.index,
         product_sales.values)
plt.title("Product Revenue")
plt.xlabel("Revenue")

# 6. Category Revenue (Line Chart)
plt.subplot(2,3,6)
plt.plot(category_sales.index,
         category_sales.values,
         marker="o")
plt.title("Category Revenue Trend")
plt.xlabel("Category")
plt.ylabel("Revenue")
plt.grid()

plt.tight_layout()
plt.savefig("project2.jpg")
plt.show()




