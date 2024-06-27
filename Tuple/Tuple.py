#Size of Tuple in bytes
tuple=(1,2,3,4)
print(len(tuple).to_bytes)

#Pg to print the element and its cude in list of tuple
list1=[]
list2=[]
ele=int(input("Enter the no of elements:"))
for i in range(0,ele):
    x=int(input("Enter the element:"))
    list2.append(x)
    list1.append(pow(x,3))
data=list(zip(list2,list1))
print(data)

#Adding tuple to List and Vice Versa
list=[]
tuple=(1,2,3)
for i in tuple:
    list.append(i)
print(list)

tuple=()
list=[1,2,3]
for i in list:
    tuple=tuple+(i,)
print(tuple)

#Sum of tuple elements
tuple=(1,2,3,4)
sum=0
for i in tuple:
    sum+=i
print(sum)

#Update each element with 4 added to it
original_list = [(1, 3, 4), (2, 4, 6), (3, 8, 1)]
updated_list = [(x+4, y+4, z+4) for (x, y, z) in original_list]
print(updated_list)

#Multiple Adjancency elements
tuple=(1,5,7,8,10)
final_tuple=()
for i in range(len(tuple)-1):
    ans= tuple[i] * tuple[i+1]
    final_tuple=final_tuple+(ans,)
print(final_tuple)


    
    


