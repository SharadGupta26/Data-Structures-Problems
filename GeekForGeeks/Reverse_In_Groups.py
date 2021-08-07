"""
Given an array arr[] of positive integers of size N. Reverse every sub-array group of size K.

 

Example 1:

Input:
N = 5, K = 3
arr[] = {1,2,3,4,5}
Output: 3 2 1 5 4
Explanation: First group consists of elements
1, 2, 3. Second group consists of 4,5.
"""

class Solution:	
    #Function to reverse every sub-array group of size k.
	def reverseInGroups(self, arr, N, k):
		# code here
		i=0
		j = i + k-1
		while j < N :
		    s,e = i,j
		    while s < e :
		        arr[s], arr[e] = arr[e], arr[s]
		        s += 1
		        e -= 1
		    i += k
		    j = i+k-1
		if i < N-1 :
		    s = i
		    e = N-1
		    while s < e :
		        arr[s], arr[e] = arr[e], arr[s]
		        s += 1
		        e -= 1