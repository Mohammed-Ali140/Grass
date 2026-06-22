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




fig, ax = plt.subplots(2, 3, figsize=(16,9))

fig.suptitle("E-Commerce Sales Analysis Dashboard", fontsize=18)

# 1 Category Wise Sales
ax[0,0].bar(category_sales.index, category_sales.values)
ax[0,0].set_title("Category Wise Sales")
ax[0,0].set_xlabel("Category")
ax[0,0].set_ylabel("Revenue")

# 2 City Wise Sales
ax[0,1].pie(city_sales.values,
            labels=city_sales.index,
            autopct="%1.1f%%")
ax[0,1].set_title("City Wise Sales")

# 3 Product Wise Sales
ax[0,2].plot(product_sales.index,
             product_sales.values,
             marker="o")
ax[0,2].set_title("Product Wise Sales")
ax[0,2].set_xlabel("Product")
ax[0,2].set_ylabel("Revenue")
ax[0,2].tick_params(axis="x", rotation=20)
ax[0,2].grid(True)

# 4 Sales Distribution
ax[1,0].hist(df["Total_Sales"], bins=5)
ax[1,0].set_title("Sales Distribution")
ax[1,0].set_xlabel("Sales")
ax[1,0].set_ylabel("Frequency")

# 5 Product Revenue
ax[1,1].barh(product_sales.index,
             product_sales.values)
ax[1,1].set_title("Product Revenue")
ax[1,1].set_xlabel("Revenue")

# 6 Category Revenue Trend
ax[1,2].plot(category_sales.index,
             category_sales.values,
             marker="o")
ax[1,2].set_title("Category Revenue Trend")
ax[1,2].set_xlabel("Category")
ax[1,2].set_ylabel("Revenue")
ax[1,2].grid(True)


plt.tight_layout()
plt.savefig("project2.jpg")
plt.show()




