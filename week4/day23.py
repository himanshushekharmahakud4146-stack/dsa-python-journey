# ============================================================
# Day 23
# HackerRank: List Operations + Sorting
# Notebook Practice: Time Complexity Thinking
# ============================================================

"""
Day 23 Summary
--------------
Focus:
- List manipulation
- Built-in sorting methods
- Understanding time complexity of sorting

Concepts Used:
- list.append()
- list.remove()
- sorted()
- list.sort()
- Big-O notation

Time Complexity:
- Append: O(1)
- Remove: O(n)
- Sorting: O(n log n)

Space Complexity:
- Depends on operation (mostly O(1))
"""

# ============================================================
# SECTION 1: HackerRank Practice
# Topic: List Operations
# ============================================================

#Basic Data Types list
    N = int(input())
    lst =[]

    for _ in range(N):
        command = input().split()

        if command[0] == "insert":
            lst.insert(int(command[1]),int(command[2]))
        elif command[0] == "print":
            print(lst)
        elif command[0] == "append":
            lst.append(int(command[1]))
        elif command[0] == "reverse":
            lst.reverse()
        elif command[0] == "pop":
            lst.pop()
        elif command[0] == "sort":
            lst.sort()
        elif command[0] == "remove":
            lst.remove(int(command[1]))
                        


#Basic Data TypesList Comprehensions
x = int(input())
y = int(input())
z = int(input())
n = int(input())

result = [
    [i,j,k]
    for i in range(x+1)
    for j in range(y+1)
    for k in range(z+1)
    if i + j + k != n
]
print(result)


# ============================================================
# SECTION 2: Sorting Practice
# ============================================================

# Python Built-InsAthlete Sort
n,m = map(int,input().split())
arr = []

for _ in range (n):
    arr.append(list(map(int,input().split())))

k = int(input())
arr = sorted(arr,key = lambda row : row[k])
for row in arr:
    print(*row)


# ============================================================
# SECTION 3: Notebook Practice
# Time Complexity Thinking
# ============================================================

"""
Why is sorting O(n log n)?

Because most efficient sorting algorithms
like Merge Sort and Timsort divide the list
into smaller parts and merge them.

Operations:
- Loop through list once → O(n)
- Nested loops → O(n²)
- Sorting → O(n log n)
"""

# Example Time Complexity Demo

def linear_search(arr, target):
    for element in arr:
        if element == target:
            return True
    return False

print("Linear Search Result:", linear_search([1,2,3,4,5], 3))


# ============================================================
# END OF DAY 23
# ============================================================
