# To filter odd and even numbers using Lambda
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers from list:", even_numbers)

odd_numbers = list(filter(lambda x: x % 2!= 0, numbers))
print("Odd numbers from the list:", odd_numbers)

#To square and cube every number in a give list of integers using lambda
numbers=[1,2,3,4,5,6,7,8,9,10]
squared = list(map(lambda x: x**2,numbers))
cube = list(map(lambda x: x**3,numbers))
print("Squared: ",squared)
print("cube:",cube)

#To find if a given string starts with a given character using lambda
string = "Hello, World!"
character = "H"
starts_with = lambda s, c: s.startswith(c)

if starts_with(string, character):
    print(f"The string '{string}' starts with '{character}'.")
else:
    print(f"The string '{string}' does not start with '{character}'.")


#Extracting year, month, date and time using lambda
from datetime import datetime
now = datetime.now()

year = lambda x: x.year
month = lambda x: x.month
date = lambda x: x.day
hour = lambda x: x.hour
minute = lambda x: x.minute
second = lambda x: x.second

print("Year:", year(now))
print("Month:", month(now))
print("Date:", date(now))
print("Hour:", hour(now))
print("Minute:", minute(now))
print("Second:", second(now))

#Finding the length of odd and even numbers using Lambda
lists=[2,5,3,4,6,4,3,6]
even_num=list(filter(lambda x: x%2==0,lists))
odd_num=list(filter(lambda x: x%2!=0 , lists))
print(len(even_num))
print(len(odd_num))

#Adding two given list using map and lambda
list1=[1,2,3]
list2=[4,5,6]
sum=list(map(lambda x,y : x+y, list1,list2))
print(sum)

#Finding numbers divisible by nineteen or thirteen from a list of numbers using lambda
list1=[19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
divisible=list(filter(lambda x : x%13==0 or x%19==0, list1))
print(divisible)

#Multiplying each number in a list with a given number using lambda
list1=[2,4,6,9,11]
multiply=2
multiplied_result= list(map(lambda x: x*multiply, list1))
print(multiplied_result)

#Mean values of elements from input list
import functools
list1=[2,4,6,9,11]
sum=functools.reduce(lambda x,y : x+y ,list1 )
mean=sum/len(list1)
print(mean)


