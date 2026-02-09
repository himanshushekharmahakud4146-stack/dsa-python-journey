# Day 12 – Collections.Counter and Majority Element
# Platforms: HackerRank + LeetCode
# Author: Himanshu

# -----------------------------
# HackerRank: Collections.Counter
# -----------------------------
from collections import Counter
n = int(input())
size = list(map(int,input().split()))
stock = Counter(size)

N = int(input())
money = 0

for _ in range(N):
    size,price = map(int,input().split())

    if stock[size]>0:
        money += price
        stock[size]-=1
print(money)

# -----------------------------
# LeetCode 169: Majority Element
# -----------------------------
class Solution:
    def majorityElement(self, nums) -> int:
        from collections import Counter
        n = Counter(nums)

        return n.most_common(1)[0][0]

s = Solution()
nums = [2,2,1,1,1,2,2]
print(s.majorityElement(nums))

# -----------------------------
# Notebook Practice: dict.get() vs Counter
# -----------------------------
#1.Build a dictionary that stores frequency of each number.
from collections import Counter

nums = [1,2,2,3,3,3]
n = Counter(nums)
print(n)
#Q2 — Find the Most Frequent Element
nums = [1,2,2,3,3,3]
d ={}
for n in nums:
    d[n] = d.get(n,0)+1
print(max(d,key=d.get))

# Q3 — First Non-Repeating Element
from collections import Counter
nums = [4,5,1,2,1,2,4]
freq = Counter(nums)
for i in nums :
    if freq[i] == 1:
        print(i)
        break

#✅ Q4 — Count Characters in a String
s = "aabbbcc"
d = {}

for ch in s:
    d[ch] = d.get(ch,0)+1

print(d)
#✅ Q5 — Top K Frequent Elements (Mini interview style)
from collections import Counter
nums = [1,1,1,2,2,3]
k = 2

freq = Counter(nums)

result = []

for x in freq.most_common(k):
    result.append(x[0])

print(result)


