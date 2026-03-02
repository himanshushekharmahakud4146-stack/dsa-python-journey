# ============================================================
# Day 25
# HackerRank: Dictionary + Sorting
# LeetCode: 242 - Valid Anagram (Redo Without Help)
# Notebook Practice: Speed Coding (30 Minutes)
# ============================================================

"""
Day 25 Summary
--------------
Focus:
- Dictionary frequency counting
- Sorting comparison method
- Writing solution without external help
- Improving coding speed

Concepts Used:
- dict()
- get() method
- sorted()
- Time complexity comparison

Time Complexity:
- Sorting approach: O(n log n)
- Dictionary approach: O(n)

Space Complexity:
- O(n)
"""

# ============================================================
# SECTION 1: HackerRank Practice
# Topic: Dictionary + Sorting
# ============================================================

# Example: Count frequency of elements in a list

def frequency_count(arr):
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    return freq

print("Frequency Count:", frequency_count([1,2,2,3,3,3]))

#collection.Counter()
from collections import Counter
n = int(input())
size = list(map(int,input().split()))
stuck = Counter(size)

N = int(input())
money = 0

for _ in range(N):
    size,price = map(int,input().split())

    if stuck[size] > 0:
        money += price
        stuck[size] -=1

print(money)

# DefaultDict Tutorial
from collections import defaultdict

n, m = map(int, input().split())

d = defaultdict(list)

# Read Group A
for i in range(1, n + 1):
    word = input().strip()
    d[word].append(i)

# Read Group B
for _ in range(m):
    query = input().strip()
    if query in d:
        print(*d[query])
    else:
        print(-1)




# ============================================================
# SECTION 2: LeetCode 242
# Valid Anagram
# ============================================================

"""
Problem:
Given two strings s and t, return True if t is an anagram of s,
otherwise return False.
"""

#242. Valid Anagram
class Solution :
    def inAnagram(self,s,t):
        if len(s) != len(t):
            return False

        d = {}

        for ch in s:
            d[ch] = d.get(ch,0)+1

        for ch in t:
            if ch not in d:
                return False
            else:
                d[ch] -= 1
            if d[ch] == 0:
                del d[ch]
        return len(d) == 0

sol = Solution()
s = "anagram"
t = "nagaram"

print(sol.inAnagram(s,t))
        


# ============================================================
# SECTION 3: Notebook Practice
# Speed Coding Session (30 Minutes)
# ============================================================

#Write code to count frequency of elements in a list
s = list(map(int,input().split()))
d ={}
for ch in s:
    d[ch] = d.get(ch,0)+1

print(d)
    
#Print element with maximum frequency

s = "absbdbfhhhhhhhe"
d = {}

for ch in s:
    d[ch] = d.get(ch,0)+1

print(max(d , key = d.get))

#Check if two strings are anagrams

s ="rac"
t ="car"

d = {}

if len(s) != len (t):
    print(False)
    exit()

for ch in s:
    d[ch] = d.get(ch,0)+1

for ch in t:
    if ch not in d:
        print(False)
        exit()
    else:
        d[ch] -= 1
        
    if d[ch] == 0:
        del d[ch]

print(True)

#Find first non-repeating character
s = "aabbcdde"
d = {}

for ch in s:
    d[ch] = d.get(ch,0)+1

for ch in s:
    if d[ch] == 1:
        print(ch)
        break

#Reverse words in a sentence
s = "I love data science"
words = s.split()

words = words[::-1]
print(" ".join(words))
    

#Find second largest number in a list

n = [10, 5, 20, 8]

first = second = float("-inf")

for x in n:
    if x>first:
        second = first
        first = x
    elif x > second and x != first:
        second = x
print(second)
      
# ============================================================
# END OF DAY 25
# ============================================================
