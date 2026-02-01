# Day 4 – Lists + Logic Practice
# Author: Himanshu

# HackerRank – Runner-Up Score
n = int(input())
arr = list(map(int,input().split()))

unique = list(set(arr))
unique.sort()

print(unique[-2])


# LeetCode – 1431 Kids With the Greatest Number of Candies
class Solution:
    def kidsWithCandies(self, candies,extraCandies):
        maximum = max(candies)
        result = []

        for i in candies :
            if i + extraCandies >= maximum:
                result.append(True)
            else:
                result.append(False)

        return result

# Notebook Practice – Runner-Up (without help)
#1.Write code to print the largest number.
nums = [4, 9, 2, 7, 5]
x = None

for i in nums:
    if x is None or i > x:
        x = i

print(x)

#Q2 — Remove Duplicates
nums = [2, 3, 6, 6, 5]
y = []

for i in nums:
    if i not in y:
        y.append(i)
print(y)
#3.Second Largest
n = int(input())
arr = list(map(int,input().split()))

unique = list(set(arr))
unique.sort()

print(unique[-2])

