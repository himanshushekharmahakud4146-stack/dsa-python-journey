# Day 15 – Python Strings Practice
# Platforms: HackerRank + LeetCode
# Author: Himanshu
# Focus: String methods and palindrome logic

# =================================================
# HackerRank: Python Strings
# Topics: capitalize(), swapcase()
# =================================================

def solution (s):
    result = []
    new_word = True

    for ch in s:
        if ch == " ":
            new_word = True
            result.append(ch)
        else:
            if new_word and ch.isalpha():
                result.append(ch.upper())
            else:
                result.append(ch)
            new_word = False
    return ''.join(result)

s = 'hello world'

print(solution(s))


# =================================================
# LeetCode 125: Valid Palindrome
# =================================================

class Solution:
    def isPalindrome(self, s):
        left , right = 0 , len(s)-1

        while left < right:
            while left < right and not s[left].isalnum():
                left +=1
            while left< right and not s[right].isalnum():
                right -=1

            if s[left].lower() != s[right].lower():
                return False
            else:
                left +=1 
                right -=1

        return True

sol = Solution()
s = "A man, a plan, a canal: Panama"
print(sol.isPalindrome(s))


# =================================================
# Notebook Practice: 10 String Method Examples
# =================================================

#Question 1: Convert to Lowercase & Count
def count_a(s: str):
    c = s.lower()
    return c.count("a")
    
s = "Data Analytics and AI"
print(count_a(s))

#Question 2: Remove Extra Spaces
def remove_spaces(s):
    return s.strip()
s = "   I love Python   "
print(remove_spaces(s))

#Question 3: Split Sentence into Words
def split_words(s):
    return s.split()
s = "machine learning is powerful"
print(split_words(s))

#Question 4: Join Words with Hyphen
def join_with_hyphen(words):
    return "-".join(words)
words = ['data', 'science', 'rocks']
print(join_with_hyphen(words))

#uestion 5: Replace a Word
def replace_bad(s):
    return s.replace('bad','good')
s = "This is a bad example"
print(replace_bad(s))

#Question 6: Find Position of a Word
def find_science(s):
    return s.find("science")

s = "data science is fun"
print(find_science(s))

#Question 7: Count a Character
def count_e(s):
    return s.count("e")
s = "experience"
print(count_e(s))

#Question 8: Check Alphanumeric
def check_alnum(s):
    return s.isalnum()
print(check_alnum("abc123"))
print(check_alnum("abc 123"))

#Question 9: Check Start and End
def check_file_name(s):
    st =  s.startswith('data')
    ed = s.endswith('.csv')
    return (st,ed)
s = "data_analysis.csv"
print(check_file_name(s))

#Question 10: Clean and Join Words
def clean_and_join(s):
    l = s.lower()
    splt = l.split()  
    return "_".join(splt)
    
s = "   I Love   Data Science   "
print(clean_and_join(s))

