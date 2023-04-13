class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        row = len(grid)
        result = [[0]*(row-2) for _ in range(row-2)]
        for i in range(row-2): 
            for j in range(row-2): 
                result[i][j] = max(grid[r][c] for r in range(i, i+3) for c in range(j, j+3))
        return result 