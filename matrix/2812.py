""" 
2812. Find the Safest Path in a Grid
Type - Medium (seems Hard)

Topics - Array, Binary Search, Breadth-First Search, Union Find, Matrix

You are given a 0-indexed 2D matrix grid of size n x n, where (r, c) represents:

    - A cell containing a thief if grid[r][c] = 1
    - An empty cell if grid[r][c] = 0

You are initially positioned at cell (0, 0). In one move, you can move to any adjacent cell in the grid, including cells containing thieves.

The safeness factor of a path on the grid is defined as the minimum manhattan distance from any cell in the path to any thief in the grid.

Return the maximum safeness factor of all paths leading to cell (n - 1, n - 1).

An adjacent cell of cell (r, c), is one of the cells (r, c + 1), (r, c - 1), (r + 1, c) and (r - 1, c) if it exists.

The Manhattan distance between two cells (a, b) and (x, y) is equal to |a - x| + |b - y|, where |val| denotes the absolute value of val.


Example 1:
Input: grid = [[1,0,0],[0,0,0],[0,0,1]]
Output: 0
Explanation: All paths from (0, 0) to (n - 1, n - 1) go through the thieves in cells (0, 0) and (n - 1, n - 1).

Example 2:
Input: grid = [[0,0,1],[0,0,0],[0,0,0]]
Output: 2
Explanation: The path depicted in the picture above has a safeness factor of 2 since:
- The closest cell of the path to the thief at cell (0, 2) is cell (0, 0). The distance between them is | 0 - 0 | + | 0 - 2 | = 2.
It can be shown that there are no other paths with a higher safeness factor.

Example 3:
Input: grid = [[0,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,0]]
Output: 2
Explanation: The path depicted in the picture above has a safeness factor of 2 since:
- The closest cell of the path to the thief at cell (0, 3) is cell (1, 2). The distance between them is | 0 - 1 | + | 3 - 2 | = 2.
- The closest cell of the path to the thief at cell (3, 0) is cell (3, 2). The distance between them is | 3 - 3 | + | 0 - 2 | = 2.
It can be shown that there are no other paths with a higher safeness factor.

 
Constraints:
    1 <= grid.length == n <= 400
    grid[i].length == n
    grid[i][j] is either 0 or 1.
    There is at least one thief in the grid.
"""

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        def calculateSafeness(grid, safenessGrid, i, j, queue, visited):
            while queue:
                size = len(queue)
                while size:
                    r, c, safe = queue.pop(0)
                    safenessGrid[r][c] = safe

                    if c + 1 < len(grid[0]) and (r, c+1) not in visited:
                        queue.append((r, c+1, safe+1))
                        visited.add((r, c+1))
                    if r + 1 < len(grid) and (r+1, c) not in visited:
                        queue.append((r+1, c, safe+1))
                        visited.add((r+1, c))
                    if c - 1 > -1 and (r, c-1) not in visited:
                        queue.append((r, c-1, safe+1))
                        visited.add((r, c-1))
                    if r-1 > -1 and (r-1, c) not in visited:
                        queue.append((r-1, c, safe+1))
                        visited.add((r-1, c))
                    size -= 1
            return safenessGrid


        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return 0

        safenessGrid = [[float('inf') for _ in range(len(grid[0]))] for _ in range(len(grid))]
        queue = []
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    queue.append((i, j, 0))
                    visited.add((i, j))
                    
        dist = calculateSafeness(grid, safenessGrid, i, j, queue, visited)

        max_heap = [(-dist[0][0], 0, 0)]
        max_safeness = [[-1] * len(grid) for _ in range(len(grid))]
        max_safeness[0][0] = dist[0][0]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while max_heap:
            d, r, c = heapq.heappop(max_heap)
            d = -d
            if r == len(grid) - 1 and c == len(grid) - 1:
                return d  

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < len(grid) and 0 <= nc < len(grid):
                    new_safe = min(d, dist[nr][nc])
                    if new_safe > max_safeness[nr][nc]:
                        max_safeness[nr][nc] = new_safe
                        heapq.heappush(max_heap, (-new_safe, nr, nc))

        return -1 
    
        


