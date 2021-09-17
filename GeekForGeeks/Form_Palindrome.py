"""
Given a string, find the minimum number of characters to be inserted to convert it to palindrome.
For Example:
ab: Number of insertions required is 1. bab or aba
aa: Number of insertions required is 0. aa
abcd: Number of insertions required is 3. dcbabcd


Example 1:

Input: str = "abcd"
Output: 3
Explanation: Inserted character marked
with bold characters in dcbabcd
Example 2:

Input: str = "aa"
Output: 0
Explanation:"aa" is already a palindrome.

sol https://www.geeksforgeeks.org/minimum-insertions-to-form-a-palindrome-dp-28/
"""


class Solution:
    def countMin(self, Str):
        # code here
        return self.minInsert(Str, 0, len(Str)-1,{})
        
    def minInsert(self,s, l,h,mem) :
        if l >= h :
            return 0
        if s[l:h+1] in mem :
            return mem[s[l:h+1]]
        if s[l] == s[h] :
            ans = self.minInsert(s, l+1, h-1, mem)
            
            #return self.minInsert(s, l+1, h-1, mem)
        else :
            ans = min(self.minInsert(s,l+1,h, mem) , self.minInsert(s,l,h-1, mem)) + 1
            #return min(self.minInsert(s,l+1,h, mem) , self.minInsert(s,l,h-1, mem)) + 1
        mem[s[l:h+1]] = ans
        return ans