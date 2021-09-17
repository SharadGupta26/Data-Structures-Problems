#User function Template for python3
""""
Given a string S, find the longest palindromic substring in S. Substring of string S: S[ i . . . . j ] where 0 ≤ i ≤ j < len(S). Palindrome string: A string which reads the same backwards. More formally, S is palindrome if reverse(S) = S. Incase of conflict, return the substring which occurs first ( with the least starting index).


Example 1:

Input:
S = "aaaabbaa"
Output: aabbaa
Explanation: The longest Palindromic
substring is "aabbaa".
Example 2:

Input: 
S = "abc"
Output: a
Explanation: "a", "b" and "c" are the 
longest palindromes with same length.
The result is the one with the least
starting index.
https://www.geeksforgeeks.org/must-do-coding-questions-for-companies-like-amazon-microsoft-adobe/

solution : https://www.geeksforgeeks.org/longest-palindrome-substring-set-1/
https://www.geeksforgeeks.org/longest-palindromic-substring-set-2/
"""
class Solution:
    def longestPalin(self, S):
        arr = [[-1 for i in range(len(S))] for i in range(len(S))]
        for i in range(len(S)) :
            arr[i][i] = 1
        ans = 0
        for i in range(len(S)) :
            for j in range(len(arr[i])):
                self.check(S,arr,i, j)
        #print(arr)
        ans = max(max(arr[i]) for i in range(len(arr)))
        #print(ans)
        for i in range(len(arr)) :
            for j in range(i,len(arr[i])) :
                if arr[i][j] == ans :
                    #print(i,j)
                    return S[i:j+1]
            
    def check(self, s, arr, i, j) :
        if i > j :
            return 2
        if arr[i][j] != -1 :
            return arr[i][j]+2
        if s[i] == s[j] :
            ans = self.check(s,arr,i+1, j-1)
            arr[i][j] = ans
            if ans > 0 :
                ans += 2
            return ans
        else :
            arr[i][j] = 0
            return 0
            