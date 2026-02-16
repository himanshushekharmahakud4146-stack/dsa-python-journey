# Day 19 – Word Frequency and Two-Pointer Logic
# Platforms: File Practice + LeetCode
# Author: Himanshu
# Focus: Word counting using dictionary and string reversal logic

# =================================================
# File Practice: Word Frequency Counter
# =================================================
#1.
fname = "words.txt"
fhand = open(fname)

counts = {}

for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

print(counts)


# =================================================
# LeetCode 344: Reverse String
# =================================================

class Solution:
    def reverseString(self, s) :
        left = 0
        right = len(s) - 1

        while left < right:
            s[left],s[right] = s[right] , s[left]
            left += 1
            right -= 1

        return s

        
sol = Solution()
s = ["h","e","l","l","o"]
print(sol.reverseString(s))


# =================================================
# Notebook Practice: split() + dict.get() Mastery
# =================================================

#Word Frequency from File
fname = 'words.txt'
fhand = open(fname)

counts ={}

for line in fhand:
    line = line.lower()
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0)+1

print(counts)

#2.Most Frequent Word

s = "Good service good food good experience"
s = s.split()
counts = {}

for line in s:
    words = line.lower()
    counts[words] = counts.get(words,0)+1

print(max(counts ,key = counts.get))

#3.Unique Word Counter
s = "Win money Win prizes now"
s = s.lower().split()
counts = {}

for line in s :
    counts [line] = counts.get(line,0)+1

print(len(counts))


#4.Reverse Each Word in a Sentence
s = "data science is fun"
s = s.split()
d = []
for ch in s:
    line = list(ch)
    left ,right = 0 ,len(ch) - 1 
    
    while left < right:
        line[left] ,line[right] = line[right],line[left]
        left +=1
        right -=1

    d.append("".join(line))

print(" ".join(d))

#5.First Non-Repeating Word
s = "hello hi hello welcome hi bye"
s = s.lower().split()
counts = {}

for words in s :
    counts[words] = counts.get(words,0)+1

for word in s:
    if counts[word] == 1:
        print (word)
        break
        
