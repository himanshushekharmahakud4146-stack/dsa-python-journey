# ============================================================
# Day 26
# Mock Test Day – 5 Timed Easy Problems
# LeetCode: 704 - Binary Search
# ============================================================

"""
Day 26 Summary
--------------
Focus:
- Timed problem solving
- Strengthening fundamentals
- Binary Search clarity

Mock Test Rules:
- Solve 5 random easy problems
- 30–45 minutes total
- No notes, no help
- Focus on speed + correctness

Concepts Used:
- Arrays
- Condition checks
- Loops
- Binary Search

Time Complexity:
- Binary Search: O(log n)

Space Complexity:
- O(1)
"""

# ============================================================
# SECTION 1: Mock Practice Problems
# (Example placeholders – replace with your actual problems)
# ============================================================

# Example Problem 1: Find maximum in list

def find_max(arr):
    maximum = arr[0]
    for num in arr:
        if num > maximum:
            maximum = num
    return maximum

print("Mock Test - Max:", find_max([1, 7, 3, 9, 2]))


# ============================================================
# SECTION 2: LeetCode 704
# Binary Search
# ============================================================

"""
Problem:
Given a sorted array of integers and a target value,
return its index if found, otherwise return -1.
"""

class Solution:
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

            
        return -1

nums = [-1,0,3,5,9,12] 
target = 9

s = Solution()
print(s.search(nums,target))



# ============================================================
# SECTION 3: Test Cases
# ============================================================

#1 704 Binary Search
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        
        return -1

# ============================================================
# END OF DAY 26
# ============================================================
