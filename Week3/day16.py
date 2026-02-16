# Day 16 – File Handling and String Cleanup
# Platforms: File Practice + LeetCode
# Author: Himanshu
# Focus: Reading files line by line, strip(), startswith()

# =================================================
# File Practice: Read File Line by Line
# =================================================

# Example file content simulation using a list
# (In real usage, this data comes from a file)
#1.
fname = input("Enter the file name: ")
fhand = open(fname)

for line in fhand:
    line = line.strip()
    if line.startswith("ERROR"):
        print(line)
 #2.
fname = input("Enter the file name: ")
fhand = open(fname)

for line in fhand:
    line = line.strip()
    parts = line.split()

    name = parts[0]
    marks = int(parts[1])

    if marks >= 40:
        print(name)


# =================================================
# LeetCode 58: Length of Last Word
# =================================================
class Solution:
    def lengthOfLastWord(self, s):
        s = s.strip()
        words = s.split()
        return len(words[-1])
      
sol = Solution()
print(sol.lengthOfLastWord("Hello World"))


# =================================================
# Notebook Practice: startswith() and strip()
# =================================================

#1.Q1 — String Cleaning & Analysis
s = "   Data   Science   is   powerful   "
count = 0
l = s.split()
for ch in l:
    count +=1
print("Total words: ",count)
print("Last word: ",l[-1])

#2.Given a sentence, print all words that start with the letter “a” or “A”.
s = "AI and analytics are amazing areas"
s = s.split()
for ch in s:
    if ch.startswith("a") or ch.startswith("A"):
        print(ch)

#3.Count how many times each word appears in a sentence.
s = "data science data ai data"
s = s.lower()
l = s.split()
d = {}

for ch in l :
    d[ch] = d.get(ch,0)+1
   
print(d)
#You are given a string containing words and numbers.
#Print only numbers greater than 50.

s = "marks are 45 78 90  in 70 32 67"
s = s.split()
for n in s:
    try:
        n = int(n)
        if n > 50:
            print (n)
    except :
        continue

#Q5 — Reverse Words
ch = "python is easy"
s = list (ch)
l = 0
r = len(s) -1

while l < r:
    s[l],s[r] = s[r],s[l]
    l += 1
    r -= 1

ch = ''.join(s)
print (ch)
