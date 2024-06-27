"""
1. Check if a number is divisible by 2,3,4
If a number is divisible by 2, print “divide by 2”
If a number is divisible by 3, print “divide by 3”
If a number is divisible by 4, print “divide by 4”

"""
num=int(input("Enter a number:"))
if num%2==0 and num%4==0:
    print("Divide by both 2 and 4")
elif num%2==0:
    print("Divide by 2")
elif num%3==0:
    print("Divide by 3")
elif num%4==0:
    print("Divide by 4 ")
else:
    print("Not divisible by 2,3 and 4")

"""
Print Grade based on marks
Mark > 90 - print O grade
Mark > 80 - print A grade
Mark > 70 - print B grade
Mark > 60 - print C grade
Mark > 50 - print D grade
Mark < 50 - print fail
"""
marks=int(input("Enter the marks:"))
if marks>90:
    print("Grade O")
elif marks>80:
    print("Grade A")
elif marks>70:
    print("Grade B")
elif marks>60:
    print("Grade C")
elif marks>50:
    print("Grade D")
else:
    print("Fail")

"""
  Write a program to find the given number is odd or even
 write the program about the fizzbuzz
 if the number is divisible by 3 print(Fizz)
 if the number is divisible by 5 print(buzz)
 if the number is divisible by 3 and 5 print(Fizzbuzz)

"""

num=int(input("Enter a number:"))
if  num%3==0 and num%5==0:
    print("Fizzbuzz")
elif num%3==0:
    print("Fizz")
elif num%5==0:
    print("buzz")

