
"""
Given a list of non negative integers, arrange them in such a manner that they form the largest number possible.The result is going to be very large, hence return the result in the form of a string.


Example 1:

Input: 
N = 5
Arr[] = {3, 30, 34, 5, 9}
Output: 9534330
Explanation: Given numbers are {3, 30, 34,
5, 9}, the arrangement 9534330 gives the
largest value.
Example 2:

Input: 
N = 4
Arr[] = {54, 546, 548, 60}
Output: 6054854654
Explanation: Given numbers are {54, 546,
548, 60}, the arrangement 6054854654 
gives the largest value.
https://www.geeksforgeeks.org/must-do-coding-questions-for-companies-like-amazon-microsoft-adobe/
"""
from functools import cmp_to_key


class Solution:

	def printLargest(self,arr):
	    #arr.sort(key = cmp_to_key(comapre) reverse = True)
	    x = cmp_to_key(self.compare)
	    arr = sorted(arr, key = x, reverse = True)
	    #print(arr)
	    return int("".join(arr))
	    
    def compare(self, a,b) :
        if int(a+b) > int(b+a) :
            return 1
        else :
            return -1
