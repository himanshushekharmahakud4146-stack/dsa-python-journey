# Day 8 – Dictionaries & Maps
# Platforms: HackerRank + LeetCode
# Author: Himanshu

# HackerRank: Dictionaries & Maps
n = int(input())
phone = {}

# Step 1: store phone book
for i in range(n):
    name, number = input().split()
    phone[name] = number

# Step 2: read queries until no more input
while True:
    try:
        q = input()

        if q in phone:
            print(q + "=" + phone[q])
        else:
            print("Not found")

    except EOFError:
        break


# LeetCode 1: Two Sum
class Solution:
    def twoSum(self, nums, target):

        seen = {}

        for i in range(len(nums)):
            need = target - nums[i]

            if need in seen:
                return [seen[need],i]

            seen[nums[i]] = i


# Notes / Practice
#1.Create a dictionary and store:"apple" → 10",banana" → 5
d = {}
d["apple"] = 10
d["banana"] = 5
print(d["banana"])
#2.Create a dictionary that counts how many times each number appears.
nums = [1, 2, 2, 3]
counts = {}

for w in nums:
    counts[w]= counts.get(w,0)+1
print(counts)
#3.Create a dictionary to count each word.
text = "i love python i love"
w = text.split()
d = {}

for i in w:
    d[i] = d.get(i,0)+1

print(d)
#Count Characters
text = "banana"

count = {}

for ch in text:
    count[ch] = count.get(ch, 0) + 1

print(count)
# Count Numbers
nums = [1, 2, 2, 3, 1, 1]
find = {}

for n in nums:
    find[n] = find.get(n,0)+1
print(find)
