
# class Ali:
#     def __init__(self,name):
#         self.name = name;
#     def show(self):
#         print(self.name)

# r = Ali("hello")
# r.show()

# class Ali:
#     def __init__(self,name,age)
#       print("Calling Constructor")
    
#     def show():
#        print("Show the Name")

    
# class Ali:

#     def __init__(self,name,age):
#      self.name = name
#      self.age = age
    
#     def getAge(self):
#        print("Age is : ",self.age)

#     def



# class Ali:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def getage(self):
#         print("My age is:", self.age)

#     def get_name(self):
#         print("My name is:", self.name)


# m = Ali("hello", 19)

# m.getage()
# m.get_name()


# 17 --> 10:32

# class Student:
#     def __init__(self,*args):
#         self.data = args


# class Student:
#     def __init__(self,*args):
#         self.data=args

#     def users(self):
#         for i in self.data[0]:
#             print(i)

#     def details(self):
#         for i in self.data[1]:
#             print(self.data[1][i])

# s=Student(["Aa","Bb","Cc","Dd"],{"address":"kukas","college":"arya","loc":"jaipur"})
# s.users()
# s.details()


# class Address:
#     # city = "Jaipur"
#     # state = "Rajasthan"
#     def __init__(self,city,state):
#      self.city = city
#      self.state = state

# a = Address("jaipur","Rajasthan")
# print(a.state)

class Address:

    def __init__(self,city,state):
     self.city = city
     self.state = state
    
    def show(self):
       print("The city is: ",self.city)

a = Address("jaipur","Rajasthan")
a.show()