import matplotlib.pyplot as plt
score = [10,20,30,40]
over = [1,2,3,4]
plt.plot(score, over)
# plt.show()


x = [2010,2015,2020,2025] # x cord
y = [100,200,250,300] # y cord.
plt.plot(x,y) # Line graph
plt.xlabel("Years") # x label
plt.ylabel("Sales") # y label
plt.title("Sales Report") # graph title
# plt.show() # graph show



x = [2010, 2015, 2020, 2025]
y = [100, 200, 250, 300]
# graph size
plt.figure(figsize=(6, 2))
# plt.plot(x, y)
# plt.show()


x = [2010, 2015, 2020, 2025]
y = [100, 200, 250, 300]
# plt.plot(x, y, color="green", marker="o", linestyle="dashed", linewidth=2, markersize=10)
# plt.show()




import matplotlib.pyplot as plt
x = [2010,2015,2020,2025] # x cord
y = [100,200,250,300] # y cord.
# *Markers*

# |character      |  |  |description |
# |-------------|  -------------------------------|
# |'.'       | | |point marker|
# |','       | | |pixel marker|
# |'o'       | | |circle marker|
# |'v'       | | |triangle_down marker|
# |'^'       | | |triangle_up marker|
# |'<'       | | |triangle_left marker|
# |'>'       | | |triangle_right marker|
# |'1'       | | |tri_down marker|
# |'2'       | | |tri_up marker|
# |'3'       | | |tri_left marker|
# |'4'       | | |tri_right marker|
# |'8'       | | |octagon marker|
# |'s'       | | |square marker|
# |'p'       | | |pentagon marker|
# |'P'       | | |plus (filled) marker|
# |'*'       | | |star marker|
# |'h'       | | |hexagon1 marker|
# |'H'       | | |hexagon2 marker|
# |'+'       | | |plus marker|
# |'x'       | | |x marker|
# |'X'       | | |x (filled) marker|
# |'D'       | | |diamond marker|
# |'d'       | | |thin_diamond marker|
# |'|'       | | |vline marker|
# |'_'       | | |hline marker|

# *Line Styles*

# |character      |  |  |  |description |
# |-------------|   -------------------------------|
# |'-'       | | | |solid line style|
# |'--'      | | | |dashed line style|
# |'-.'      | | | |dash-dot line style|
# |':'       | | | |dotted line style|

# Example format strings:

#     'b'    # blue markers with default shape
#     'or'   # red circles
#     '-g'   # green solid line
#     '--'   # dashed line with default color
#     '^k:'  # black triangle_up markers connected by a dotted line
# *Colors*

# |character      |  |  |  |color |
# |-------------|   -------------------------------|
# |'b'       | | | |blue|
# |'g'       | | | |green|
# |'r'       | | | |red|
# |'c'       | | | |cyan|
# |'m'       | | | |magenta|
# |'y'       | | | |yellow|
# |'k'       | | | |black|
# |'w'       | | | |white|
# graph size
plt.figure(figsize=(6,2)) # width or height
plt.plot(x,y,color="y",marker='*',linestyle=":",linewidth=4,markersize=14,)
# plt.show()



# multi lines chart
import matplotlib.pyplot as plt
x = [2010,2015,2020,2025]
y1 = [100,200,260,290]
y2 = [150,185,195,300]

plt.plot(x,y1,label="jeans")
plt.plot(x,y2,label="shirt")
plt.xlabel("years")
plt.ylabel("sales")
plt.title("Sales Report")
plt.legend() # info of label
plt.show()


# Question 1
import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May"]

sales_A = [100, 120, 140, 130, 150]
sales_B = [90, 110, 135, 145, 160]
sales_C = [80, 100, 120, 125, 140]

plt.plot(months, sales_A, marker='o', label='Product A')
plt.plot(months, sales_B, marker='s', label='Product B')
plt.plot(months, sales_C, marker='^', label='Product C')

plt.title("Monthly Sales Comparison")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.legend()
plt.grid(True)
plt.show()


# Question 2
import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed", "Thu", "Fri"]

city1 = [30, 32, 31, 33, 35]
city2 = [28, 29, 30, 31, 32]
city3 = [25, 27, 26, 28, 29]

plt.figure(figsize=(8,5))

plt.plot(days, city1, marker='o', label="Jaipur")
plt.plot(days, city2, marker='s', label="Delhi")
plt.plot(days, city3, marker='^', label="Mumbai")

plt.title("Temperature Comparison")
plt.xlabel("Days")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.grid(True)
plt.show()


# Bar Chart
import matplotlib.pyplot as plt
x = [2015,2020,2025,2030]
y = [100,150,200,290]

# size
plt.figure(figsize=(6,2)) 
plt.bar(x,y)
plt.show()


# Multi Bar Chart
import matplotlib.pyplot as plt
import numpy as np
x = np.array([1,2,3,4])
y1 = [10,20,20,40]
y2 = [20,30,25,30]
# calculation -> width
w = 0.40
plt.bar(x - w/2,y1 , label="boys",width=w) 
plt.bar(x + w/2,y2, label="girls",width=w) 

plt.xlabel("groups")
plt.ylabel("number of students")
plt.title("Number of Students in Each group")
plt.legend()
# plt.show()

import numpy as np
 
x = np.arange(4)
 
y1 = [1, 1.2, 2.3, 1.2]
y2 = [1.5, 1.4, 1, 3.2]
y3 = [4, 3, 2, 1]
 
w = 0.25
 
plt.bar(x - w, y1, width=w, label="2023", color="lightblue")
plt.bar(x,     y2, width=w, label="2024", color="blue")
plt.bar(x + w, y3, width=w, label="2025", color="lightgreen")
 
plt.xticks(x, ["Vehicle", "Home", "Work", "Office"])
plt.yticks([0, 1, 2, 3, 4], ["0", "1M", "2M", "3M", "4M"])
 
plt.title("Sales Comparison by Location")
plt.xlabel("Location")
plt.ylabel("Sales (Millions)")
 
plt.grid(axis="y")
plt.legend()
plt.show()