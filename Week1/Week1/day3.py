# Day 3 – Lists Practice
# Author: Himanshu

#HackerRank: List Comprehensions
# Let's learn about list comprehensions! You are given three integers  and  representing the dimensions of a cuboid along with an integer . Print a list of all possible coordinates given by  on a 3D grid where the sum of  is not equal to . Here, . Please use list comprehensions rather than multiple loops, as a learning exercise.
x = int(input())
y = int(input())
z = int(input())
n = int(input())
results = [[i,j,k]
          for i in range(x+1)
          for j in range(y+1)
          for k in range(z+1)
          if i + j + k != n
          ]
print(results)

#LeetCode: 2011 Final Value of Variable After Performing Operations
class Solution:
    def finalValueAfterOperations(self, operations):
        x = 0

        for op in operations:
            if "+" in op:
                x += 1
            else :
                x -=1
        return x

# Notes Practice
#1.Create a list of squares from 1 to 5 using list comprehension.
squres = [ i*i  for i in range(1,6)]
print(squres)

#2. nums = [1,2,3,4,5,6,7,8,9,10] #Create a new list containing only EVEN numbers
nums = [1,2,3,4,5,6,7,8,9,10]
evens = [ i for i in nums if i%2 == 0]
print(evens)

#3. Using list comprehension, store each character of: "Himanshu"
names = 'Himanshu'
char = [c for c in names]
print(char)

  
