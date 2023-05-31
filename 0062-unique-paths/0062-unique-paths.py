class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[0 for i in range(n)] for _ in range(m)]
        memo[0][0] = 1
        row = m
        col = n
        for r in range(row):
            for c in range(col):
                
                if 0 <= r - 1 <= row - 1:
                    memo[r][c] += memo[r - 1][c] 
                if 0 <= c - 1 <= col - 1:
                     memo[r][c] += memo[r][c - 1]
                      
        return memo[-1][-1]