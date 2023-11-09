class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        R,C = len(grid), len(grid[0])
        perimeter = 0
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    perimeter += 4
                    if i>0 and grid[i-1][j] == 1:
                        perimeter -= 2
                    if j>0 and grid[i][j-1] == 1:
                        perimeter -= 2
        return perimeter