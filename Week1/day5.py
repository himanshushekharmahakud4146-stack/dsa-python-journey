# Day 5 – Nested Lists + Logic Practice
# Author: Himanshu

# HackerRank – Nested Lists
students = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    students.append([name,score])

scores = []
for s in students:
    scores.append(s[1])

scores = sorted(set(scores))
second_last = scores[1]

names = []
for s in students:
    if s[1] == second_last:
        names.append(s[0])

for name in sorted(names):
    print(name)
    
# LeetCode – 1672 Richest Customer Wealth
class Solution:
    def maximumWealth(self, accounts):
        max_wealth = 0

        for customer in accounts:
            wealth = sum(customer)
            max_wealth = max(max_wealth, wealth)

        return max_wealth


# Notebook Practice – Sorting + Nested Lists

#1.Write a program to print: 1 2 3 4 5 (using loop)

a = []
for i in range(1,6):
    a.append(i)

print(a)
    

#2.Sum of list Given: nums = [2,4,6] Find total using loop.
nums = [2,4,6]
t = 0

for i in nums:
    t = i+t
print(t)

#3.Count elements
a = [10,20,30,40]
count = 0

for i in a:
    count+=1

print(count)

#4.Largest number
nums = [5,3,9,1]
lst = 0

for i in nums:
    if i > lst:
        lst = i

print(lst)

#5.Even numbers
nums = [1,2,3,4,5,6]
E = []

for i in nums:
    if i%2 == 0 :
        E.append(i)
print(E)

#6.Double values
nums = [1,2,3]
D = []

for i in nums:
    a = i*2
    D.append(a)

print(D)

#7.Reverse list
a = [1,2,3,4]
rev = []

for i in range(len(a)-1,-1,-1):
    rev.append(a[i])
print(rev)

#8.Count positives
nums = [-2,3,-1,5,0]
count = 0

for i in nums:
    if i > 0:
        count += 1

print(count)

#9.Find average
marks = [50,60,70]
s = 0
count = 0

for i in marks:
    s = i+s
    count += 1
print(s/count)

#10.Nested list sum
data = [[1,2],[3,4]]
t = 0

for i in data:
    for j in i:
        t += j

print(t)

  

