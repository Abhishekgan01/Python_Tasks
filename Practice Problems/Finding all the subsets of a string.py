str = input("Enter a string:")
n = len(str);  
arr = [];  
   
for i in range(0,n):  
    for j in range(i,n):  
        arr.append(str[i:(j+1)]);  
     
print("All subsets for given string are: ");  
for i in arr:  
    print(i);  

#Sample input and output
'''
Enter a string:ABCDEF
All subsets for given string are: 
A
AB
ABC
ABCD
ABCDE
ABCDEF
B
BC
BCD
BCDE
BCDEF
C
CD
CDE
CDEF
D
DE
DEF
E
EF
F
'''