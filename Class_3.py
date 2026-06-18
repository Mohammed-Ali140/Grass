
# num_1 = 10
# num_2 = 20

# if num_1 < num_2:
#     print(num_2)

# num1 = input(" Enter the Number: ")
# if num1:
#     print("Number : ",num1)

# else:
#     print("zero",num1)

# age = int(input(" Enter Your Age: "))
# if age == 18:
#     print("Your Age is : ", age)
# elif age > 18:
#     print("You are above then 18 : ",age)
# else:
#     print("You are less than : ", age)

# marks = int(input("Enter your Marks: "))

# if (marks >= 90 and marks <=100):
#     print("Grade A:",marks)

# elif(marks >= 75 and marks < 90):
#     print("grade B:",marks)

# elif(marks >= 60 and marks < 75):
#     print("grade C:",marks)

# else:
#     print("FAIL:",marks)



#  ****** LOOPS ******

# for i in range(6):
#     print("i = ",i)

# for i in range(1, 11):
#     print("i = ",i)

# list 
# l = [1,2,3,4]
# print(len(l))

# # for i in range(4):
# for i in range(len(l)):
#   print(l[i])

# for i in l:
#   print(i)

# While loops

# num1 = int(input("Enter the Number: "))
# i = 0
# while i < num1:
#     print(i)
#     i+=1

# l = [10,11,12,13,14,15]
# i = 0
# while i < len(l):
#     print(l[i])
#     i+=1

# num = int(input("Enter a Number: "))
# count = 0
# while num > 0:
#     num //= 10
#     count +=1
# print(count)   

# L = [10,[11,12,13,14,15]]
# #To print the element 11, 12, 13, 14 , 15 we have two methods
# for i in range(len(L[1])):      # 1st Method
#     print(L[1][i])

# for i in L[1]:                #2nd Method
#     print(i)

# To print 13 , 14 , 15
# for i in range(2,len(L[1])):
#     print(L[1][i])

# num = int(input("Enter A number: "))
# i = 1
# j = i
# while i <= num:
#     while j > 0:
#        print("*")

    

# Break
# for i in range(5):
#     if i == 2:
#         break
#     print(i)

# # Continue
# for i in range(4):
#     if i == 2:
#         continue
#     print(i)

# i = 0
# while True:
#     print(i)
#     if i == 5:
#         break
#     else:
#         i += 1
#         continue

 # Pass

# i = 0
# while True:
#     print(i)
#     if i == 4:
#         pass
#     if i == 5:
#         break
#     else:
#         i += 1
#         continue
