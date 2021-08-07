"""
Given an array A of n positive numbers. The task is to find the first Equilibium Point in the array. 
Equilibrium Point in an array is a position such that the sum of elements before it is equal to the sum of elements after it.

Example 1:

Input:
n = 1
A[] = {1}
Output: 1
Explanation: Since its the only element hence its the only equilibrium 
point. 
Example 2:

Input:
n = 5
A[] = {1,3,5,2,2}
Output: 3
Explanation: For second test case 
equilibrium point is at position 3 
as elements before it (1+3) = 
elements after it (2+2).

https://www.geeksforgeeks.org/must-do-coding-questions-for-companies-like-amazon-microsoft-adobe/
"""

class Solution:
    # Complete this function
    
    #Function to find equilibrium point in the array.
    def equilibriumPoint(self,A, N):
        # Your code here
        total = sum(A)
        running_sum = 0
        if N == 1 :
            return 1
        for i in range(N) :
            val = A[i]
            if running_sum == total - val -running_sum :
                return i+1
            running_sum += val
        return -1