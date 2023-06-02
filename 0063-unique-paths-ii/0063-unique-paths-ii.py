class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        if obstacleGrid[row - 1][col - 1] == 1:
            return 0
        memo = [[0 for i in range(col)] for _ in range(row)]
        memo[0][0] = 1
        
        for r in range(row):
            for c in range(col):
                
                if 0 <= r - 1 <= row - 1 and obstacleGrid[r - 1][c] != 1:
                    memo[r][c] += memo[r - 1][c] 
                if 0 <= c - 1 <= col - 1 and obstacleGrid[r][c - 1] != 1:
                     memo[r][c] += memo[r][c - 1]
                      
        return memo[-1][-1]