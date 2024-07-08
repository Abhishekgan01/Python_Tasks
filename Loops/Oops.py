#Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
class Vehicle:
    name="Car"
    wheel=4
    colour="red"

class Bus(Vehicle):
    colour="Blue"
    
obj=Bus()
print(obj.name)
print(obj.colour)#Overriding

#Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.
class Circle:
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return 3.14*self.radius**2
    
    def perimeter(self):
        return 2*3.14*self.radius
    
r=int(input("Enter the radius:"))
obj=Circle(r)
print(obj.area())
print(obj.perimeter())

#Write a Python program to create a calculator class. Include methods for basic arithmetic operations.
class Calculator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2

    def add(self):
        return self.num1+self.num2
    
    def subtract(self):
        return self.num1-self.num2
    
    def multiplication(self):
        return self.num1*self.num2
    
    def division(self):
        return self.num1/self.num2

a=int(input("Enter number 1:"))
b=int(input("Enter number 2:"))


#Write a Python program to create a class that represents a shape. Include methods to calculate its area and perimeter. Implement subclasses for different shapes like circle, triangle, and square.
import math

class Shape:
    def __init__(self):
        pass

    def area(self):
        pass

    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def perimeter(self):
        return self.a + self.b + self.c


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side

circle = Circle(5)
print("Circle area:", circle.area())
print("Circle perimeter:", circle.perimeter())

triangle = Triangle(3, 4, 5)
print("Triangle area:", triangle.area())
print("Triangle perimeter:", triangle.perimeter())

square = Square(4)
print("Square area:", square.area())
print("Square perimeter:", square.perimeter())


#Write a Python program to create a person class. Include attributes  like name, country and date of birth. Implement a method to  determine the person’s age
from datetime import datetime

class Person:
    def __init__(self,name,country,date_of_birth):
        self.name=name
        self.country=country
        self.date_of_birth = date_of_birth
    
    def age_calculate(self): 
        return datetime.now().year - self.date_of_birth


name=input("Enter the name:")
country=input("Enter the country:")
date_of_birth=int(input("Enter the date of :"))
obj1=Person(name,country,date_of_birth)
print(obj1.age_calculate())


#Write a Python program to create two empty classes, Student and Marks. Now create some instances and check whether they are instances of the said classes or not. Also, check whether the said classes are subclasses of the built-in object class or not.
class A:
    pass

class B:
    pass

a=A()
b=B()
print(isinstance(a,A))
print(isinstance(b,B))
print(issubclass(A,B))


#Create a class named Student with two attributes student_name, marks. Modify the attribute values of the said class and print the original and modified values of the said attributes.
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    @property
    def msg(self):
        return self.name + " and " + str(self.marks) 
    
    
stud=Student("Abhi",80)
print(stud.msg)
stud.marks=90
print(stud.msg)

#Write a Python class named Student with two attributes: student_id, student_name. Add a new attribute: student_class. Create a function to display all attributes and their values in the Student class.
class Student:
    def __init__(self, student_id, student_name, student_class):
        self.student_id = student_id
        self.student_name = student_name
        self.student_class = student_class

    def display_attributes(self):
        print(f"Student ID: {self.student_id}")
        print(f"Student Name: {self.student_name}")
        print(f"Student Class: {self.student_class}")

student1 = Student(1, "Abhishek", "MCA")
student2=Student(2,"Akash","MCA")
student1.display_attributes()
student2.display_attributes()

#---------Advanced-------#
#Write a Python program to create a class representing a shopping cart. Include methods for adding and removing items, and calculating the total price. 
class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item_name, price, quantity=1):
        item = {"name": item_name, "price": price, "quantity": quantity}
        self.items.append(item)
        print(f"Added {quantity} x {item_name} to the cart.")

    def remove_item(self, item_name, quantity=1):
        for item in self.items:
            if item["name"] == item_name:
                if item["quantity"] > quantity:
                    item["quantity"] -= quantity
                    print(f"Removed {quantity} x {item_name} from the cart.")
                elif item["quantity"] == quantity:
                    self.items.remove(item)
                    print(f"Removed {item_name} from the cart.")
                else:
                    print(f"Cannot remove {quantity} x {item_name}. Only {item['quantity']} in the cart.")
                break
        else:
            print(f"{item_name} not found in the cart.")

    def total_price(self):
        total = sum(item["price"] * item["quantity"] for item in self.items)
        return total

    def show_cart(self):
        if not self.items:
            print("The cart is empty.")
        else:
            print("Shopping Cart:")
            for item in self.items:
                print(f"{item['quantity']} x {item['name']} = ${item['price']} each")

cart = ShoppingCart()
cart.add_item("Apple", 0.99, 3)
cart.add_item("Banana", 0.59, 2)
cart.show_cart()
print(f"Total price: ${cart.total_price():.2f}")
cart.remove_item("Apple", 1)
cart.show_cart()
print(f"Total price: ${cart.total_price():.2f}")


#Stack implementation
#First method
stack=[]
stack.append(3)
stack.append(7)
stack.pop()
print(stack)

#Second Method
from collections import deque
stack=deque([1,2,3])
print(stack)
stack.appendleft(5)
print(stack)

#Queue Implementation
from queue import Queue
q=Queue()
q.put(1)
q.put(2)
a=q.get(1)
print(a)

#Linked List Implementation (Add, remove and display)
class Node:
    def __init__(self, data):
        self.data=data
        self.pointer=None

class LinkedList:

    def __init__(self):
        self.head=None
    
    def add(self,data):
        newNode=Node(data)
        if self.head is None:
            self.head=newNode
        else:
            cur = self.head
            while (cur.pointer is not None):
                cur=cur.pointer
            cur.pointer=newNode

    def remove(self,data):
        if(self.head is not None):
            if(self.head.data==data):
                self.head=self.head.pointer
            else:
                cur=self.head
                while(cur.pointer is not None and cur.pointer.data!=data):
                    cur=cur.pointer
                if cur.pointer is not None:
                    cur.pointer=cur.pointer.pointer
        else:
            print("It is empty")

    def print(self):
        cur =self.head
        while (cur is not None):
            print(cur.data)
            cur=cur.pointer

linkedlist = LinkedList()
linkedlist.add(1)
linkedlist.add(2)
linkedlist.add(3)
linkedlist.add(4)
linkedlist.remove(2)
linkedlist.print()


