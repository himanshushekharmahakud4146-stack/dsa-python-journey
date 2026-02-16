# Day 18 – Dictionary Patterns and Array Logic
# Platforms: File Practice + LeetCode
# Author: Himanshu
# Focus: Hour distribution using dictionary and array increment logic

# =================================================
# File Practice: Hour Distribution (Q10.2 Style)
# =================================================

#hour distribution (like Q10.2)
fname = 'activity_log.txt'
fhand = open(fname)
d = {}

for line in fhand:
    if line.startswith('From '):
        line = line.split()
        time = line[5]
        time = time.split(':')
        t = time[0]
        if t in d:
            d[t] +=1
        else:
            d[t] = 1

for k,v in sorted(d.items()):
    print(k,v)


# =================================================
# LeetCode 66: Plus One
# =================================================

#66 Plus One
class Solution :
    def plusOne(self,digits):

        for i in range(len(digits)-1,-1,-1):
            if digits[i]<9:
                digits[i]+=1
                return digits
            else:
                digits[i] = 0
             
        return [1] + digits
s = Solution()
digits = [4,3,2,9]

print(s.plusOne(digits))


# =================================================
# Notebook Practice: Repeat Logic Without Looking
# =================================================

#1.
fname = 'activity_log.txt'
fhand = open(fname)
d = {}
for line in fhand:
    if line.startswith('From '):
        line = line.split()
        time = line[5]
        t = time.split(':')
        tm = t[0]
        if tm in d:
            d[tm] += 1
        else:
            d[tm] = 1
for k,v in sorted(d.items()):
    print(k,v)

#2.
class Solution:
    def plusOne(self,digits):
        for i in range(len(digits)-1,-1,-1):
            if digits[i] < 9 :
                digits[i] +=1
                return digits
            else:
                digits[i] = 0
        return [1] + digits


s = Solution()
digits = [1,2,3,9,9,9,9]
print (s.plusOne(digits))
