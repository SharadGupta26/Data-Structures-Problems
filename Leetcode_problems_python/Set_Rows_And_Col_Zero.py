"""Given an m x n matrix. If an element is 0, set its entire row and column to 0. Do it in-place.

Follow up:

A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?

https://leetcode.com/problems/set-matrix-zeroes/
"""

from typing import List

#O(m+n) space solution
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = set()
        cols = set()
        for i in range(len(matrix)) :
            for j in range(len(matrix[i])) :
                if matrix[i][j] == 0 :
                    rows.add(i)
                    cols.add(j)
        for i in range(len(matrix)) :
            for j in range(len(matrix[i])) :
                if i in rows or j in cols: 
                    matrix[i][j] = 0



#another solution not using set to store index. 
#using recursion
import math
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        for i in range(len(matrix)) :
            for j in range(len(matrix[i])) :
                if matrix[i][j] == 0 :
                    self.row_zero(matrix, i)
                    self.col_zero(matrix, j)
                    
        for i in range(len(matrix)) :
            for j in range(len(matrix[i])) :
                if matrix[i][j] == math.inf :
                    matrix[i][j] = 0
        
    def row_zero(self, matrix, rowNo) :
        row = matrix[rowNo]
        for colNo in range(len(row)) :
            if row[colNo] == 0 :
                row[colNo] = math.inf
                self.col_zero(matrix, colNo)
            else :
                row[colNo] = math.inf
            
    def col_zero(self, matrix, colNo) :
        for rowNo in range(len(matrix)) :
            if matrix[rowNo][colNo] == 0 :
                matrix[rowNo][colNo] = math.inf
                self.row_zero(matrix, rowNo)
            else :
                matrix[rowNo][colNo] = math.inf


#their solution , constant space
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        is_col = False
        R = len(matrix)
        C = len(matrix[0])
        for i in range(R):
            # Since first cell for both first row and first column is the same i.e. matrix[0][0]
            # We can use an additional variable for either the first row/column.
            # For this solution we are using an additional variable for the first column
            # and using matrix[0][0] for the first row.
            if matrix[i][0] == 0:
                is_col = True
            for j in range(1, C):
                # If an element is zero, we set the first element of the corresponding row and column to 0
                if matrix[i][j]  == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        # Iterate over the array once again and using the first row and first column, update the elements.
        for i in range(1, R):
            for j in range(1, C):
                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j] = 0

        # See if the first row needs to be set to zero as well
        if matrix[0][0] == 0:
            for j in range(C):
                matrix[0][j] = 0

        # See if the first column needs to be set to zero as well        
        if is_col:
            for i in range(R):
                matrix[i][0] = 0