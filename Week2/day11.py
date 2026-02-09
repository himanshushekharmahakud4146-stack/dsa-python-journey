# Day 11 – String Split, Join and Unique Character
# Platforms: HackerRank + LeetCode
# Author: Himanshu


# HackerRank: String Split and Join
s = "this is a string"
s = s.split(" ")
print(s)

s = "-".join(s)
print(s)

# LeetCode 387: First Unique Character in a String
# -----------------------------
class Solution:
    def firstUniqChar(self, s):
        count ={}

        for ch in s:
            count[ch] = count.get(ch,0)+1

        for i in range(len(s)):
            if count[s[i]] == 1:
                return(i)

        return -1

S = Solution()
s = "loveleetcode"
print(S.firstUniqChar(s))

# Practice: split() and join()
# -----------------------------
text = "  i   love   python  "
words = text.split()
print(words)

joined = "_".join(words)
print(joined)
#11️ Use .split() to convert it into a list of words.
s = "python is very powerful"
print(s.split())
#2.Use .join() to convert this list into ONE string separated by -
words = ["machine", "learning", "is", "cool"]
w = '-'.join(words)
print(w)
#3.1️⃣ Split the string into words #2️⃣ Join them back using _ (underscore)
s = "i love artificial intelligence"
s = s.split()
print("_".join(s))
#4.
s = "data science and machine learning"
s = s.upper()
s = s.split()
print("-".join(s))
#5.
s = "  i   love   python  "
s = s.split()
print("-".join(s))


# -----------------------------

