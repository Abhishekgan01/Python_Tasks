#Iterate over a set in Python
set={"abhi","shek","raja"}
for i in set:
    print(i)
    
#Min and Max elements in a Set
set={1,2,3,4,5}
min_ele=min(set)
max_ele=max(set)
print(min_ele)
print(max_ele)

#Finding common elements in three lists
arr1 = [1, 5, 10, 20, 40, 80]
arr2 = [6, 7, 20, 80, 100]
arr3 = [3, 4, 15, 20, 30, 70, 80, 120]

set1 = set(arr1)
set2 = set(arr2)
set3 = set(arr3)

common_elements = list(set1 & set2 & set3)
print("Common elements:", common_elements)

#Check if two lists have at-least one element common
a=[1,2,3,4,5]
b=[5,6,7,8,9]
for i in a:
    if i in b:
        print("There is atleast a common element")

#Difference between two lists
list1 = [10, 15, 20, 25, 30, 35, 40]
list2 = [25, 40, 35]

set1=set(list1)
set2=set(list2)

difference = list(set1-set2)
print(difference)

#Python program to count number of vowels using sets in given string
string=input("Enter a string:")
vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
count = 0
for i in string:
    if i in vowels:
        count+=1
print(count)

#Python Program to Accept the Strings Which Contains all Vowels
string=input("Enter a string:")
vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
converted=set(string)
if vowels.issubset(string):
    print("All Vowels Present:")

#Python set to check if a String is a panagram
string=input("Enter a string:")
alphabet=set('qwertyuioplkjhgfdsazxcvbnm')
converted=set(string.lower())
if alphabet.issubset(string):
    print("It is a panagram")

#Python program to convert Set into Tuple and Tuple into Set
set={1,2,3,4,5}
tuple=()
for i in set:
    tuple=tuple + (i,)
print(tuple)

tuple = (1, 2, 3, 4, 5)
converted_set = set(tuple)
print(converted_set)

# Convert Set to String in Python
set={1,2,3,4,5}
converted=str(set)
print(converted)
print(type(converted))

