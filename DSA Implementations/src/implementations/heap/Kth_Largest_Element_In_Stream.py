"""
Given an input stream arr[] of n integers. Find the Kth largest element for each element in the stream and if the Kth element doesn't exist, return -1.

Example 1:

Input:
k = 4, n = 6
arr[] = {1, 2, 3, 4, 5, 6}
Output:
-1 -1 -1 1 2 3

"""

import heapq
class Solution:
    def kthLargest(self, k, arr, n):
        # code here 
        heap = []
        res = []
        for i in arr :
            if len(heap) < k :
                heapq.heappush(heap, i)
            elif i > heap[0] :
                heapq.heappop(heap)
                heapq.heappush(heap, i)
            
            if len(heap) < k :
                res.append(-1)
            else :
                res.append(heap[0])
        return res