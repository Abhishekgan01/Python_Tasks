# # # A generator function that yields 1 for first time,
# # # 2 second time and 3 third time
# # def simpleGeneratorFun():
# #     yield 1,2            
             
 
# # # Driver code to check above generator function
# # for value in simpleGeneratorFun(): 
# #     print(value)

# def multiple_yield():  
#     str1 = "First String"  
#     yield str1  
  
#     str2 = "Second string"  
#     yield str2  
  
#     str3 = "Third String"  
#     yield str3  
# obj = multiple_yield()  
# print(next(obj))  
# print(next(obj))  
# print(next(obj))  

# list = [1,2,3,4,5,6]  
  
# z = (x**3 for x in list)  
  
# print(next(z))  
  
# print(next(z))  


# def multiple_yield():  
#     str1 = "First String"  
#     yield str1  
  
#     str2 = "Second string"  
#     yield str2  
  
#     str3 = "Third String"  
#     yield str3  
# obj = multiple_yield()  
# print(obj)

def count_up_to(max):
    count = 1
    while count <= max:
        yield count  # Produces a value and pauses
        count += 1

# Using the generator
gen = count_up_to(3)
print(next(gen))  # Output: 1
print(next(gen)) 


