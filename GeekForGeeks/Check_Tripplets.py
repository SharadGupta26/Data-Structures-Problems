"""
Given an array arr of N integers, write a function that returns true if there is a triplet (a, b, c) that satisfies a2 + b2 = c2, otherwise false.

Example 1:

Input:
N = 5
Arr[] = {3, 2, 4, 6, 5}
Output: Yes
Explanation: a=3, b=4, and c=5 forms a
pythagorean triplet.
Example 2:

Input:
N = 3
Arr[] = {3, 8, 5}
Output: No
Explanation: No such triplet possible.

"""
class Solution:

	def checkTriplet(self,arr, n):
        arr = [i**2 for i in arr]
        data = set(arr)
        for i in arr :
            for j in arr :
                if i-j in data :
                    return True
        return False