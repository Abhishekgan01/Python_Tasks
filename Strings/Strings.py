
words=input("Enter the string:")
print(words[::-1])

#Methods 
a="abHiaBhi"
print(a.startswith(a)) 
print(a.endswith(a))
print(a.index("b")) 
print(a.title())
print(a.upper())
print(a.lower())
print(a.swapcase())
print(a.count("a"))
print(a.find("a",1))
print(a.strip())
print(a.isalpha())
print(a.isalnum())
print(a.islower())
print(a.isupper())
print(a.isspace())
print(a.isnumeric())

string = input("Enter a string:")
list=[]
for i in string:
    list.append(i)
print(list)
for i in range(len(list),0):
    print(list[i])

#Reverse a string using loop
input=input("Enter a string:")
list=""
for i in input:
    list = i + list
print(list)

#Reverse a string using stack
stack=[]
input=input("Enter a string: ")
for i in input:
    stack.append(i)
while stack:
    print(stack.pop())

#Reverse using reverse function
string = input("Enter a string:")
input= list(string)
input.reverse()
print(input)

#even length words in string
names=["abhishek", "sandeeps","vikas","rohith"]
for name in names:
    if len(name)%2==0:
        print(name)

#string has atleast one letter and one number
import re
string = input("Enter a string:")
has_letter = re.search('[a-z A-Z]', string)
has_number = re.search('[0-9]', string)
print( bool(has_letter and has_number))


#Remove duplicates
#Method 1
input=input("Enter any string:")
without_duplicate=set(input)
print(without_duplicate)

#Method 2
s=input("Enter the input:")
seen = set()
result = []
for char in s:
    if char not in seen:
        seen.add(char)
        result.append(char)
print(''.join(result))

