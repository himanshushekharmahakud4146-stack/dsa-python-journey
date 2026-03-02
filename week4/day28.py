# ============================================================
# Day 28
# Mini Project v2 Improvements
# - Top 5 words
# - Ignore stopwords
# - Export result to file
# LeetCode: 26 - Remove Duplicates from Sorted Array
# ============================================================

"""
Day 28 Summary
--------------
Focus:
- Improving existing project
- Cleaning text data
- Word frequency ranking
- Two-pointer technique

Concepts Used:
- Dictionary frequency counting
- Sorting by value
- File writing
- Two-pointer method

Time Complexity:
- Text analysis: O(n log n) due to sorting
- Remove Duplicates: O(n)

Space Complexity:
- O(n)
"""

# ============================================================
# SECTION 1: Mini Project v2 - Text Analyzer Upgrade
# ============================================================

# Step 1: input text
text = input("Enter text: ").lower()

# Step 2: stopwords list
stopwords = {"a", "the", "is", "and", "to", "of", "in", "on"}

# Step 3: remove punctuation
clean_text = ""
for ch in text:
    if ch.isalpha() or ch == " ":
        clean_text += ch

# Step 4: split into words
words = clean_text.split()

# Step 5: count frequency (ignoring stopwords)
freq = {}

for word in words:
    if word not in stopwords:
        freq[word] = freq.get(word, 0) + 1

# Step 6: sort by frequency (descending)
sorted_words = sorted(freq.items(), key=lambda x: x[1], reverse=True)

# Step 7: top 5 words
top_5 = sorted_words[:5]

# Step 8: print result
print("Top 5 words:")
for word, count in top_5:
    print(word, count)

# Step 9: export to file
with open("output.txt", "w") as f:
    for word, count in top_5:
        f.write(f"{word} : {count}\n")

print("Result saved to output.txt")


# ============================================================
# SECTION 2: LeetCode 26
# Remove Duplicates from Sorted Array
# ============================================================

"""
Problem:
Given a sorted array, remove duplicates in-place
and return the number of unique elements.
"""

class Solution:
    def removeDuplicates(self, nums) :
        if not nums:
            return 0
        k = 1

        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                nums[k] = nums[i]
                k += 1
        return k
s = Solution()
nums = [1,1,2]
print(s.removeDuplicates(nums))


# ============================================================
# SECTION 3: Test Cases
# ============================================================

sol = Solution()

nums = [1,1,2,2,3,4,4]
k = sol.removeDuplicates(nums)

print("Unique Count:", k)
print("Modified Array:", nums[:k])


# ============================================================
# END OF DAY 28
# ============================================================
