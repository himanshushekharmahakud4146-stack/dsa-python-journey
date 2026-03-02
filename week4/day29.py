# ============================================================
# Day 29
# Revision Day
# Redo:
# - Two Sum
# - Valid Anagram
# - Word Count From File
# ============================================================

"""
Day 29 Summary
--------------
Focus:
- Rewriting solutions from memory
- Strengthening dictionary usage
- Reviewing file handling logic

Concepts Revised:
- Hash map
- Frequency counting
- File reading
- Clean implementation

Time Complexity:
- Two Sum: O(n)
- Valid Anagram: O(n)
- Word Count: O(n)
"""

# ============================================================
# SECTION 1: Two Sum (Redo From Memory)
# ============================================================

class TwoSumSolution:
    def twoSum(self, nums, target):
        lookup = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in lookup:
                return [lookup[complement], i]
            lookup[num] = i

        return []


ts = TwoSumSolution()
print("Two Sum Test:", ts.twoSum([2,7,11,15], 9))  # Expected: [0,1]


# ============================================================
# SECTION 2: Valid Anagram (Redo From Memory)
# ============================================================

class AnagramSolution:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        freq = {}

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        for ch in t:
            if ch not in freq:
                return False
            freq[ch] -= 1
            if freq[ch] < 0:
                return False

        return True


an = AnagramSolution()
print("Anagram Test:", an.isAnagram("anagram", "nagaram"))  # True


# ============================================================
# SECTION 3: Word Count From File (Redo)
# ============================================================

def word_count_from_file(filename):
    freq = {}

    with open(filename, "r") as file:
        for line in file:
            words = line.strip().lower().split()
            for word in words:
                freq[word] = freq.get(word, 0) + 1

    return freq


"""
To test:
Create a sample.txt file manually
Add some words
Call function below
"""

# Example usage (uncomment after creating file)
# print(word_count_from_file("sample.txt"))


# ============================================================
# END OF DAY 29
# ============================================================
