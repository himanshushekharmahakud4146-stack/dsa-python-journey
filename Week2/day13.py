# Day 13 – Frequency Patterns and Top K Elements
# Platforms: HackerRank + LeetCode
# Author: Himanshu

# -----------------------------
# HackerRank: Word Count (Dictionary – Medium Style)
# -----------------------------
from collections import  Counter
s = input()
c =Counter(s)

items = sorted(c.items(),key=lambda x: (-x[1],x[0]))

for ch, freq in items[:3]:
    print(ch,freq)

# -----------------------------
# LeetCode 347: Top K Frequent Elements
# -----------------------------
from collections import Counter
class Solution:
    def topKFrequent(self, nums,k)-> int :
        n = Counter(nums)
        result =[]
        items = sorted(n.items(),key=lambda x: (-x[1],x[0]))

        for ns, vl in items[:k]:
            result.append(ns)

        return result

s = Solution()
nums = [1,1,1,2,2,3]
k = 2
print(s.topKFrequent(nums,k))

# -----------------------------
# Notebook Practice: Top Frequent Items Logic
# -----------------------------
data = ["a", "b", "a", "c", "b", "a"]

# Step 1: Count
d = {}
for x in data:
    d[x] = d.get(x, 0) + 1

print("Frequency dict:", d)

# Step 2: Sort by frequency
sorted_items = sorted(d.items(), key=lambda x: -x[1])
print("Sorted items:", sorted_items)

# Step 3: Take top element
top_item = sorted_items[0][0]
print("Top frequent item:", top_item)
