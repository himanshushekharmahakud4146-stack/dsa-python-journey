# ============================================================
# Day 24
# HackerRank: String Problems
# LeetCode: 3 - Longest Substring Without Repeating Characters
# Notebook Practice: Sliding Window Basics
# ============================================================

"""
Day 24 Summary
--------------
Focus:
- String traversal
- Character frequency tracking
- Sliding window technique

Concepts Used:
- set()
- dictionary for frequency
- Two pointers
- While loop window adjustment

Time Complexity:
- LeetCode 3: O(n)

Space Complexity:
- O(min(n, m)) where m = charset size
"""

# ============================================================
# SECTION 1: HackerRank Practice
# Topic: String Problems
# ============================================================

# Example: Count vowels in a string

def count_vowels(s):
    vowels = "aeiou"
    count = 0
    for char in s.lower():
        if char in vowels:
            count += 1
    return count

print("Vowel Count:", count_vowels("Himanshu"))

#Python-Strings-String Split and Join

a = input()
a = a.split()
print("-".join(a))

# Strings-What's Your Name?

first_name = input()
last_name = input()
print("Hello "+first_name+" "+last_name+"! You just delved into python.")

# Strings- sWAP cASE
s = input()
print(s.swapcase())


# ============================================================
# SECTION 2: LeetCode 3
# Longest Substring Without Repeating Characters
# ============================================================

"""
Problem:
Given a string s, find the length of the longest substring
without repeating characters.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left = 0 
        max_len = 0

        for right in range(len(s)):
            while s[right] in char_set :
                char_set.remove(s[left])
                left +=1

            char_set.add(s[right])
            max_len = max(max_len,right - left +1)

        return max_len

sol = Solution()
s = 'aaaabcvfbbcccdddhh'
print(sol.lengthOfLongestSubstring(s))


# ============================================================
# END OF DAY 24
# ============================================================
