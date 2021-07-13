"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false

https://leetcode.com/problems/search-a-2d-matrix/
"""

from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix :
            if target > row[-1] :
                continue
            else :
                return self.search(row, target, 0, len(row)-1)
        return False
            
    def search(self, row, target, i, j) :
        if j < i:
            return False
        mid = (j+i)//2
        if row[i] == target or row[j] == target or row[mid] == target:
            return True
        elif target < row[mid] :
            return self.search(row, target, i, mid-1)
        else :
            return self.search(row, target, mid + 1, j)
        