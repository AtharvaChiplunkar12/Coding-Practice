"""
1219. Path with Maximum Gold
Type - Medium

Topics - Array, Backtracking, Matrix

In a gold mine grid of size m x n, each cell in this mine has an integer representing the amount of gold in that cell, 0 if it is empty.

Return the maximum amount of gold you can collect under the conditions:
    - Every time you are located in a cell you will collect all the gold in that cell.
    - From your position, you can walk one step to the left, right, up, or down.
    - You can't visit the same cell more than once.
    - Never visit a cell with 0 gold.
    - You can start and stop collecting gold from any position in the grid that has some gold.

 

Example 1:

Input: grid = [[0,6,0],[5,8,7],[0,9,0]]
Output: 24
Explanation:
[[0,6,0],
 [5,8,7],
 [0,9,0]]
Path to get the maximum gold, 9 -> 8 -> 7.

Example 2:

Input: grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
Output: 28
Explanation:
[[1,0,7],
 [2,0,6],
 [3,4,5],
 [0,3,0],
 [9,0,20]]
Path to get the maximum gold, 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7.


Constraints:

    m == grid.length
    n == grid[i].length
    1 <= m, n <= 15
    0 <= grid[i][j] <= 100
    There are at most 25 cells containing gold.


"""

class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def path(grid, i, j, pathSum, visited):
            if i<0 or i>len(grid)-1 or j<0 or j>len(grid[0])-1:
                return pathSum
            
            currSum = pathSum
            if grid[i][j] != 0:
                pathSum+=grid[i][j]
                combinations = [[0, 1], [1, 0], [0, -1], [-1, 0]]
                visited.add((i, j))
                for u, v in combinations:
                    if (i+u,j+v) not in visited:
                        currSum = max(currSum, path(grid, i+u, j+v, pathSum, set(visited)))
            return currSum

        out = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                currSum = path(grid, i, j, 0, set())
                out = max(out, currSum)
        return out
