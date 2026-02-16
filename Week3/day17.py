# Day 17 – File Processing and Stack Logic
# Platforms: File Practice + LeetCode
# Author: Himanshu
# Focus: Extracting emails from files and stack-based validation

# =================================================
# File Practice: Extract Email from "From" Lines (mbox style)
# =================================================
#1.
fname ="test_mbox.txt"
fhand = open(fname)

for line in fhand:
    if line.startswith('From '):
        word = line.split()
        print(word[1])
#2.
count = 0 
fname = 'test_mbox.txt'
fhand = open(fname)
for line in fhand:
    if line.startswith('From'):
        words = line.split()
        print(words[1])
        count +=1
print('Total mail: ',count)


# =================================================
# LeetCode 20: Valid Parentheses
# =================================================

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', '}': '{', ']': '['}

        for ch in s:
            if ch in pairs:
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)

        return len(stack) == 0

            
   

sol = Solution()
s = "{[(])}"
print(sol.isValid(s))

# =================================================
# Notebook Practice: Create and Test Custom File Data
# =================================================

#File Handling – Count Emails
#Read the file
#Print only email addresses from lines starting with "From "
#Count how many emails are printed

fname = 'test_mbox.txt'
fhand = open(fname)
count = 0

for line in fhand:
    if line.startswith('From '):
        line=line.split()
        print(line[1])
        count+=1
print (count)


#2: File Handling – Domain Extraction
#Extract email addresses from "From " lines
#From each email, extract only the domain name

fname = 'test_mbox.txt'
fhand = open(fname)

for line in fhand:
    if line.startswith('From'):
        line = line.split('.')
        name = line[0].split()
        print(name[1])


#Valid Parentheses
s = input()
stack = []
pairs = {')':'(','}':'{',']':'['}

valid = True

for ch in s:
    if ch in pairs:
        if not stack or stack[-1] != pairs[ch]:
            valid = False
            break
        stack.pop()
    else:
        stack.append(ch)

if valid and len(stack) == 0:
    print(True)
else:
    print(False)

#Only Parentheses ( and )
s = input()
stack = []

for ch in s:
    if ch == '(':
        stack.append(ch)
    else:   # ch == ')'
        if not stack:
            print(False)
            break
        stack.pop()
else:
    if len(stack) == 0:
        print(True)
    else:
        print(False)

