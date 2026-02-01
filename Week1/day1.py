# Day 1 – Python Basics Practice
# Author: Himanshu

# HackerRank Practice - Python If-Else, Arithmetic Operators
n = int(input("Enter a integer number: "))
if n%2 != 0:
    print("Weird")
elif n%2 == 0 and (n>=2 and n<= 5 ):
    print("Not Weird")
elif n%2 == 0 and (n>=6 and n<= 20):
    print("Weird")
elif n%2 == 0 and n>20:
    print("Not Weird")

# Personal Notes Practice
#1.Check even or odd
x = int(input ('Enter a number: '))
if x%2 == 0:
        print (x," is a Even number")
else:
    print(x," is a Odd number")
#2.Check largest of two numbers
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

if x > y:
    print(x,' is largest number')
else:
    print(y," is largest number")
 #3.print numbers from 1 to 10 using for loop
for i in range(1, 11):
    print(i)
  #4. Print even numbers from 1 to 20
for x in range(1, 21):
    if x % 2 == 0:
        print(x)
#5.check positive, negative, or zero
x = input("Enter a Number: ")
try :
    y = int(x)
    if y > 0 :
        print(y,' is a positive number')
    elif y < 0:
        print(y," is a negative number")
    else:
        print(y," is Zero")
except:
    print(x," is not a integer")
    

       
        

