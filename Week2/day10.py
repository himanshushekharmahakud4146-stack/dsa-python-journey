# Day 10 – Tuples and Anagram Grouping
# Platforms: HackerRank + LeetCode
# Author: Himanshu


# HackerRank: Tuples
n = int (input())
r = map(int,input().split())

t = tuple(r)
print(hash(t))
# LeetCode 49: Group Anagrams
class Solution:
    def groupAnagrams(self, strs):
        from collections import defaultdict
        d = defaultdict(list)
        for w in strs:
            key = ''.join(sorted(w))
            d[key].append(w)

        return list(d.values())
s = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
print(s.groupAnagrams(strs))

# -----------------------------
# Notebook Practice: Tuple Sorting
t = (5, 10, 15)
print(t[1])

a,b,c = t

print(a+c)
#Dictionary → Tuple Sorting
d = {"apple": 3, "banana": 1, "orange": 2}

items = list (d.items())

Short_Of_d = sorted(items, key= lambda x: x[1])

print(Short_Of_d)
   
#Mini Anagram Group

from collections import defaultdict
words = ["cat","tac","act","dog"]

d = defaultdict(list)

for w in words:
    key = ''.join(sorted(w))
    d[key].append(w)

print(list(d.values()))
