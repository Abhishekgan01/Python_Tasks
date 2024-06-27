"""
1.write a python program to add two numbers given below a=55 and b=22
    store the answer in a new variable
    multiply the answer with a 
    store the multiplied answer in new variable 
    compare the multiplied answer with value a 
    if the answer is greater then multiply the answer with (pi)value
    increment the answer by 34
    and decrement the answer by 20 
    then compare the value of all the present solution 
"""
import math
a=55
b=22
c=a+b
print(c)
d=c*a
print(d)
if d>a:
    e=d*math.pi
    print(e)
    e+=34
    print(e)
    e-=20
    print(e)


"""
2. Write a Python program to display the examination schedule. (extract the date from     exam_st_date).
    exam_st_date = (11, 12, 2014)
    Sample Output : The examination will start from : 11 / 12 / 2014

"""
exam_st_date = (11,12,2014)
print("The examination will start from : %i/%i/%i"%exam_st_date)

# 3.Area of a Circle
import math
r=float(input("Enter the radius:"))
area=math.pi*r*r
print(area)

# 4.Area of a Triangle
b=float(input("Enter the base:"))
h=float(input("Enter the height:"))
area=0.5*b*h
print("The area is:", area)

# 5.Swapping two numbers
a=4
b=9
temp=a
a=b
b=temp
print("a",a)
print("b",b)

#6.Reverse a number
#Method 1
n=123456789
sum=0
while n>0:
    r=n%10
    sum=sum*10+r
    n=n//10
print(sum)

#Method 2
n=input("Enter the number: ")
m=n[::-1]
print(m)


