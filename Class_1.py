# a = 10             # Declaring variable
# print(a)           # used to print Value , 
                     # In python if variable have same value then there address will
                     # be same to

# a = 10
# b = 10                 # id(Value) is used to check address of value 
# print(a,b)             # and it takes ony one argume
# print(id(a), id(b))    

# a = 20
# b = a
# a = 30
# print(a,b)
# print(id(a),id(b))
  

# #float 
# b = 10.10
# print(b)
# print(type(b))  
                            
# # srting
# c = "Ali"
# print(c)
# print(type(c))  
                    
# a = int (input("Enter The Number: "))   # input(arg) is use to tak input from user
# print(a)
# print(type(a))                          # It Tells type of a 

# num = input("enter the number: ")
# print(num)
# print(type(num))
# # print(num + 10)            # Error
# print(int(num) + 10)         # Both have type integer
# print(num + str(10))         # Both have type String
# print(num * 10)              # It will print Value of mum 10 times in terminal

a = str(input("Enter The Number: "))  # now it type is str
# a = input("Enter The Number: ")    # But we dont need to add str 
print(a)
print(type(a))                          # bcz it default it is str