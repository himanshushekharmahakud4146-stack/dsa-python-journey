# ============================================================
# Day 22
# HackerRank: Basic Math + Conditions
# LeetCode: 121 - Best Time to Buy and Sell Stock
# Notebook Practice: 3 Custom Test Cases
# ============================================================

"""
Day 22 Summary
--------------
Focus:
- Strengthening condition logic
- Understanding single-pass optimization
- Practicing clean implementation

Concepts Used:
- if-else conditions
- Modulo operator
- Tracking minimum value
- Greedy approach
- Time Complexity analysis

Time Complexity:
- HackerRank Practice: O(1)
- LeetCode 121: O(n)

Space Complexity:
- O(1)
"""

# ============================================================
# SECTION 1: HackerRank Practice
# Topic: Basic Math + Conditions
# ============================================================

# Example Problem:
#1.Prepare-Mathematics-Fundamentals-Maximum Draws
t = int(input())

for _ in range(t):
    n = int(input())
    print(n+1)

#Prepare-Mathematics-Fundamentals-Find the Point
n = int(input())

for _ in range(n):
    px,py,qx,qy = map(int,input().split())
    rx = 2*qx - px
    ry = 2*qy - py 
    print(rx,ry)

#Prepare-Mathematics-Fundamentals-Find the Point
n = int(input())

for _ in range(n):
    px,py,qx,qy = map(int,input().split())
    rx = 2*qx - px
    ry = 2*qy - py 
    print(rx,ry)

#Handshakes
t = int (input())

for _ in range(t):
    n = int(input())
    print(n*(n-1)//2)

#Halloween Party
t = int(input())

for _ in range (t):
    k = int(input())
    print(k//2 * (k-(k//2)))


# ============================================================
# SECTION 2: LeetCode 121
# Best Time to Buy and Sell Stock
# ============================================================

"""
Problem Statement:
You are given a list prices where prices[i] is the price
of a stock on day i.

Find the maximum profit you can achieve.
You may buy once and sell once.
Return 0 if no profit is possible.
"""

class Solution:
    def maxProfit(self,prices):
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            else:
                profit = price - min_price
                if profit > max_profit:
                    max_profit = profit
                    
        return max_profit

prices = [1, 2, 3, 4, 5]
s = Solution()
print(s.maxProfit(prices)) max_profit


# ============================================================
# SECTION 3: Notebook Practice
# Custom Test Cases
# ============================================================

#1.maximum Draw
def maxDraw(n):
    return n+1

n = int(input())
print(maxDraw(n))

#2.Halloween Party
class Solution:
    def halloweenParty(self,k):
        a = k//2
        b = k-a

        return a*b

k = int(input())
s = Solution()
print(s.halloweenParty(k))

#3.Best Time to Buy and Sell Stock

class Solution:
    def maxProfit(self,prices):
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            else:
                profit = price - min_price
                if profit > max_profit:
                    max_profit = profit

        return max_profit

prices = [1,2,3,4,5,6,7]
s = Solution()
print(s.maxProfit(prices))

# ============================================================
# END OF DAY 22
# ============================================================
