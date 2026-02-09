# Day 9 
# Platforms: HackerRank + LeetCode
# Author: Himanshu

# HackerRank: Set .add(), Set union/intersection basics
n = int(input())
s = set()

for i in range(n):
    country = input()
    s.add(country)

print(len(s))
#Set .union() Operation
n = int(input())
s = set(input().split())
b = int(input())
r = set(input().split())
print(len(s.union(r)))
#Set .intersection() Operation
n = int(input())
E = set(map(int,input().split()))
b = int(input())
F = set(map(int,input().split()))
print(len(E.intersection(F)))


# LeetCode 1: 242 Valid Anagram
class Solution:
    def isAnagram(self, s, t):
      if len(s) != len(t):
        return False
      d={}
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
      
# Notes / Practice
#Write a Python program to count characters in this string:
s = "programming"

d = {}
for ch in s:
    d[ch] = d.get(ch,0)+1
print(d)
#Given two lists: Find common elements using sets.
a = [1,2,3,4,5]
b = [4,5,6,7]
x = set(a)
y = set(b)
print(x.intersection(y))
#Check if these two strings are anagrams:
s = "listen"
t = "silent"
d = {}

if len(s) != len(t):
    print(False)
    exist()

for ch in s:
    d[ch] = d.get(ch,0)+1

for ch in t:
    if ch not in d:
        print(False)
        exist()
    d[ch] -=1
    if d[ch] == 0:
        del d[ch] 

if len(d) == 0:
    print(True)
else:
    print(False)
#Count only VOWELS in this string:
s = "datascience"
d = {}
for ch in s:
    if ch in 'aeiouAEIOU':
        d[ch] = d.get(ch,0)+1
print(d)
#Given two strings: Find characters common in BOTH strings and print them as a set.
s1 = "aabbcc"
s2 = "bbccdd"
S1 = set(s1)
S2 = set(s2)
print(S1.intersection(S2))

