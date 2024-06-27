#1.Print from 1 to 10
num=int(input("Enter a number:"))
for i in range(1,num+1):
    print (i)

#print all the values from 1 to the number but skip values that are divisible by 10 - using continue
num=int(input("Enter a number:"))
for i in range(1,num+1):
    if i%10==0:
        continue
    else:
        print(i)

#print all the values from 1 to the number but exit the loop if i > 90
num=int(input("Enter a number:"))
for i in range(1,num+1):
    if i>90:
        break
    else:
        print(i)

#Sum of all numbers from 1 to 10
num=int(input("Enter a number:"))
sum=0
for i in range(1,num+1):
    sum=sum+i
print(sum)

#Infinite While loop with a break statement to come out of loop
while True:
    num=int(input("Enter a number:"))
    if num==10:
        break

"""
Print the following pattern using loops
		1 
2 2 
3 3 3 
4 4 4 4

"""
for i in range(1,5):
    for j in range(i):
        print(i, end='')
    print("")