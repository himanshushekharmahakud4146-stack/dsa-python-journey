# Day 20 – Mini Project Start: Text Analyzer
# Platforms: Mini Project + LeetCode
# Author: Himanshu
# Focus: Text statistics and basic array logic

# =================================================
# Mini Project: Text Analyzer (v1 logic)
# =================================================

class Solution:
    def text_analyzer(self,text ):
        text = text.lower()
        words = text.split()
        counts = {}


        if not words:
                return 0, 0, None


        for word in words:
                counts[word] = counts.get(word,0)+1

        total_words = len(words)
        unique_words = len(counts)
        most_frequent_words = max(counts,key = counts.get)

        return total_words,unique_words,most_frequent_words

text = input("Enter a text: ")
s = Solution()
total, unique, frequent =s.text_analyzer(text)

print ('Total words: ',total)
print ('Unique words: ',unique)
print("Most frequent word: ",frequent)

# =================================================
# LeetCode 268: Missing Number
# =================================================

class Solution:
    def missingNumber(self,nums):
        
        n = len(nums)
        expect_sum = n*(n+1)//2
        actual_sum = sum(nums)
        return expect_sum - actual_sum

s = Solution()
nums = list(map(int,input().split()))
print(s.missingNumber(nums))
