# ============================================================
# Day 27
# HackerRank: Sets / Unique Elements
# LeetCode: 278 - First Bad Version
# Notebook Practice: Binary Search Revision
# ============================================================

"""
Day 27 Summary
--------------
Focus:
- Understanding sets and uniqueness
- Applying binary search on answer space
- Revising binary search logic

Concepts Used:
- set()
- len(set())
- Binary search on condition
- Reducing search space

Time Complexity:
- Sets: O(n)
- Binary Search: O(log n)

Space Complexity:
- Sets: O(n)
- Binary Search: O(1)
"""

# ============================================================
# SECTION 1: HackerRank Practice
# Topic: Sets / Unique Elements
# ============================================================

#1 Python Sets Introduction to Sets

def average(array):
    s = set(array)

    return sum(s) / len(s)

array = list(map(int,input().split()))
print(average(array))
#2.Python Sets Set .add()
N = int(input())
s = set()

for i in range(N):
    country = input()
    s.add(country)

print(len(s))

#3.Python Sets Set .discard(), .remove() & .pop()
n = int(input())
s = set(list(map(int, input().split())))
N = int(input())

for _ in range(N):
    word = list(input().split())
    
    if word[0] == "pop":
        s.pop()
    elif word[0] == "remove":
        s.remove(int(word[1]))
    elif word[0] == "discard":
        s.discard(int(word[1]))
print(sum(s))
        



# ============================================================
# SECTION 2: LeetCode 278
# First Bad Version (Binary Search on Condition)
# ============================================================

"""
Problem:
You are given n versions.
You need to find the first bad version.

We simulate isBadVersion() for practice.
"""

# Simulated bad version for testing
bad_version = 4

def isBadVersion(version):
    return version >= bad_version


class Solution:
    def firstBadVersion(self, n):
        left = 1
        right = n

        while left < right:
            mid = (left + right) // 2

            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1

        return left


# ============================================================
# END OF DAY 27
# ============================================================
