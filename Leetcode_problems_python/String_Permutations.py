#User function Template for python3
from collections import deque
class Solution:
    def find_permutation(self, S):
        res = []
        elements = deque()
        elements.append([])
        for val in S :
            n = len(elements)
            for _ in range(n) :
                k = elements.popleft()
                for j in range(len(k),-1,-1) :
                    new = list(k)
                    new.insert(j,val)
                    if len(new) == len(S) :
                        res.append(''.join(new))
                    else :
                        elements.append(new)
        res.sort()
        return res
                    




# Python program to print all permutations with
# duplicates allowed
# https://www.geeksforgeeks.org/write-a-c-program-to-print-all-permutations-of-a-given-string/
 
def toString(List):
    return ''.join(List)
 
# Function to print permutations of string
# This function takes three parameters:
# 1. String
# 2. Starting index of the string
# 3. Ending index of the string.
def permute(a, l, r):
    if l==r:
        print(toString(a))
    else:
        for i in range(l,r+1):
            a[l], a[i] = a[i], a[l]
            permute(a, l+1, r)
            a[l], a[i] = a[i], a[l] # backtrack
 
# Driver program to test the above function
string = "ABC"
n = len(string)
a = list(string)
permute(a, 0, n-1)
 