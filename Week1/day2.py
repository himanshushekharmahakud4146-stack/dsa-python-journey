# Day 2 – Python Basics Practice
# Author: Himanshu

# HackerRank Practice -  Loops
n = int(input())

for i in range(n):
    print(i * i)

n = int(input())
#Print Function
for i in range(1,n+1):
    print(i,end="")
  
# LeetCode Practice
class Solution:
    def runningSum(self, nums):
        t = 0
        result = []

        for x in nums:
            t += x
            result.append(t)

        return result
