# Day 6 – Dictionary + Logic Practice
# Author: Himanshu

# HackerRank – Finding the Percentage
n = int(input())
students_marks = {}

for _ in range(n):
    name, *scores = input().split()
    scores = list(map(float,scores))
    students_marks[name] = scores
    
query_name = input()
avg = sum(students_marks[query_name])/len(students_marks[query_name])
print(f"{avg:.2f}")


# LeetCode – 217 Contains Duplicate
class Solution:
    def containsDuplicate(self,nums):
        if len(nums) != len(set(nums)):
            return True
        else :
            return False

# Notebook Practice – Dictionary Basics Revision
#Find Ravi’s average marks
marks  = {
    "Amit" : [12,34,56],
    "Ravi" :[30,45,67]
}

mark = marks["Ravi"]
s = sum(mark)

print(s/len(mark))

#Print True if duplicate exists, else False.

nums = [2, 5, 7, 2]
if len(nums) == len(set(nums)):
    print (True)
else :
    print(False)

#Create a dictionary:{"Apple":50, "Banana":30}Print Banana price.

d ={}
d['Apple'] = 50
d["Banana"] = 30
print(d['Banana'])

#Create empty dictionary and add:
d = {}
Name = "Ravi"  
Marks = 80
d[Name] = Marks
print(d)

#Given:Print all keys using loop.

d = {"A":10, "B":20}
for k,v in d.items():
    print((k))

#Check if "A" exists in dictionary.
d = {"A":10, "B":20}
if "A" in d:
    print(True)
else : print(False)

#Find length of:
d = {"x":1,"y":2,"z":3}
print(len(d))

#Update "B" value to 100.
d = {"A":10, "B":20}
d['B'] = 100
print(d)

#Delete "x" from:
d = {"x":1,"y":2,"z":3}
del d["x"]
print(d)


# Find Ram’s average.
marks = {"Ram":[50,60,70]}
avg = sum(marks["Ram"])/len(marks["Ram"])
print(f"{avg:.1f}")

#Create dictionary of 2 students and print both name + marks using loop.
n = 2
students = {}
for _ in range(n):
    name, *marks  = input().split()
    marks = list(map(float,marks))
    students[name] = marks
for k,v in students.items():
    print((k,v))
