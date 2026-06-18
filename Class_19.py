
# import matplotlib.pyplot as plt

# # Graph one data
# year = [2010,2015,2020,2025]
# dairy = [100,520,630,400]

# # Graph two data
# year = [1999,2000,2005,2010]
# farming = [300,200,250,1004]

# fig , aux = plt.subplots(1 , 2)

# aux[0].plot(year , dairy)  # First Column for line chart
# aux[0].set_xlabel("Years")
# aux[0].set_ylabel("Dairy")
# aux[0].set_title("Dairy Production Graph")

# aux[1].plot(year , dairy)  # First Column for line chart
# aux[1].set_xlabel("Years")
# aux[1].set_ylabel("Farming")
# aux[1].set_title("Farming Production Graph")
# plt.show()


#-------------------------------------------------------------------------------------------



# subplots 2d
# import matplotlib.pyplot as plt

# # graph 1
# year = [2010, 2015, 2020, 2025]
# dairy = [100, 520, 630, 400]

# # graph 2
# farming = [300, 200, 250, 100]

# # graph 3
# college = [10, 20, 25, 30]

# # graph 4
# transport = [50, 75, 100, 150]

# fig, aux = plt.subplots(2, 2)   # 4 cols

# aux[0][0].plot(year, dairy)
# aux[0][0].set_xlabel("Year")
# aux[0][0].set_ylabel("Dairy")
# aux[0][0].set_title("Dairy Production ")

# aux[0][1].bar(year, farming)
# aux[0][1].set_xlabel("Year")
# aux[0][1].set_ylabel("Farming")
# aux[0][1].set_title("Dairy Production ")

# aux[1][0].pie(year, labels = college)
# aux[1][0].set_xlabel("Year")
# aux[1][0].set_ylabel("College")
# aux[1][0].set_title("College Production ")

# aux[1][1].scatter(year, transport)
# aux[1][1].set_xlabel("Year")
# aux[1][1].set_ylabel("Transport")
# aux[1][1].set_title("Transport Production ")

# plt.tight_layout()
# plt.show()


# #------------------------------------------------------------------------------------


# import matplotlib.pyplot as plt
# students = ["A", "B", "C", "D", "E"]
# marks = [85, 90, 75, 88, 95]
 
# attendance = [80, 90, 75, 85, 95]
 
# ages = [18, 19, 18, 20, 19]
 
# fig, ax = plt.subplots(2, 2)
 
# # Line Chart
# ax[0,0].plot(students,marks,marker='o')
# ax[0,0].set_title("Marks Trend")
# ax[0,0].set_xlabel("Students")
# ax[0,0].set_ylabel("Marks")
# ax[0,0].grid(True)
 
# # Bar Chart
# ax[0,1].bar(students,attendance,color="orange")
# ax[0,1].set_title("Attendance")
# ax[0,1].set_xlabel("Students")
# ax[0,1].set_ylabel("Attendance %")
 
# # pie char
# ax[1,0].pie(ages,labels= students)
 
# # Histogram
# ax[1,1].hist(marks,bins=5,color="green",edgecolor="black")
# ax[1,1].set_title("Marks Distribution")
# ax[1,1].set_xlabel("Marks")
# ax[1,1].set_ylabel("Frequency")
 
# plt.tight_layout()
 

# # plt.gcf().canvas.get_supported_filetypes()
# plt.savefig("subplot.jpg")
# plt.show()



# #-----------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt
import pandas as pd

url = "https://raw.githubusercontent.com/rajendra0968jangid/Ds-arya/main/temperature_data.json"
df = pd.read_json(url)
# print(df)

# df.drop(2 ,axis = 0, inplace = True)
df.dropna(subset = ["temperature_c"] , inplace = True)
# print(df)

# Below line will fill all null by mean
# df.fillna(df['humidity_pct'].mean() , inplace = True)

# Below line will fill specific row by mean
df['humidity_pct'] = df['humidity_pct'].fillna(df['humidity_pct'].mean())
# print(df)

df['farenheit'] = ( df['temperature_c'] * 1.8 ) + 32
print(df)

# subplots -> 1d -> line chart | pie chart
fig,aux = plt.subplots(1,2)
aux[0].plot(df["humidity_pct"],df["temperature_c"])
aux[0].set_xlabel("Humidity")
aux[0].set_ylabel("Temperature in Celsius")
aux[0].set_title("Humidity With Celsius")
 
aux[1].pie(df["farenheit"],labels=df["day"],autopct="%1.1f%%")
aux[1].set_title("Humidity With Farenheit")
# save image data
plt.savefig("project1.pdf")
plt.show()




