"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

"""
from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = [[False for i in range(n)] for i in range(m)]
        ans = 0
        for i in range(m) :
            for j in range(n) : 
                if self.island(grid,visited,i,j) == True:
                    ans += 1
        return ans

    def island(self, grid, visited, i,j) :
        if i<0 or j<0 or i >= len(grid) or j >= len(grid[0]) :
            return False
        if visited[i][j] == True or grid[i][j] == '0':
            visited[i][j] = True
            return False
        visited[i][j] = True
        a = self.island(grid,visited, i+1,j)
        b = self.island(grid,visited, i-1, j)
        c = self.island(grid,visited, i,j+1)
        d =  self.island(grid,visited,i,j-1)
        return True or a or b or c or d