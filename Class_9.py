
# class Address:
#   def __init__(self,city,state):
#     self.city = city
#     self.state = state
  
#   def location(self):
#     return f"my location is {self.city} in {self.state}"
 
# class User(Address):
#   def __init__(self,name,age,city,state):
#     self.name = name
#     self.age = age
#     super().__init__(city,state)
#     # self.city = city
#     # self.state = state
 
#   def userName(self):
#     print(f"my name is {self.name}")
 
#   def userDetails(self):
#     print(f"my name is {self.name} and my location is {self.city} in {self.state}")
 
# u = User("Ali",20,"kukas","rajasthan")
# print(u.city)
# u.userDetails()
# u.location()
 
# a = Address("kukas","rajasthan")


# encapsulation


# class Address: 
#     def __init__(self,city,state): 
#         self.__city = city # private Attribute 
#         self.state = state

#     def location(self):
#              print(f"My location is {self.__city} in {self.state}")

#     def get_city(self):
#          return self.__city
    
# a = Address("jaipur","rajasthan") 
# a.location()
# a.get_city() # print(a.__city) 
# print(a.state)


# Polymorphism 
# class Address:
#     def __init__(self,city,state):
#         self.city = city
#         self.state = state
    
#     def location(self):
#         print(f"My Address is {self.city} in {self.state}")

# class HomeTown:
#     def __init__(self,city,state):
#         self.city = city
#         self.state = state
        
#     def location(self):
#         print(f"And My Home Town  is {self.city} in {self.state}")
        

# a = Address("Jaipur", "Rajasthan")
# a.location()
# b = HomeTown("A" ,"B")
# b.location()

# class Address:
#     total = 0
#     def __init__(self,city,state):
#         self.city = city
#         self.state = state
#         Address.total += 1
    
#     def location(self):
#         print(f"My Address is {self.city} in {self.state}")


# a = Address("Jaipur", "Rajasthan")
# print(a.total)

# Overloading --> Not Possible
# def address(city , state):
#     print(f" My Address is {city} in {state}")

# def address(city , state , country):
#     print(f" My Address is {city} in {state} in {country}")

# # address("jaipur" , " rajasthan") #Overloading not possible
# address("jaipur" , " rajasthan" , "INDIA")

# Overriding 