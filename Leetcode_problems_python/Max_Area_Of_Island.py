"""
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0."""

from itertools import product
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])
        visited = [[False for i in range(n)] for i in range(m)]
        return max((self.maxArea(grid, visited, i, j) for i, j in product(range(m), range(n))))

    def maxArea(self, grid, visited, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i]):
            return 0
        try:
            if visited[i][j] == False and grid[i][j] == 1:
                visited[i][j] = True
                a = self.maxArea(grid, visited, i+1, j)
                b = self.maxArea(grid, visited, i-1, j)
                c = self.maxArea(grid, visited, i, j+1)
                d = self.maxArea(grid, visited, i, j-1)
                return a+b+c+d+1
            else:
                visited[i][j] = True
                return 0
        except:
            return 0
