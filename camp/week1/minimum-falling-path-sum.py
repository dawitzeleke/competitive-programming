class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        memo = {}
        row = len(matrix)
        col = len(matrix[0])
        
        def dp(r, c):
            if c < 0 or c >= col:
                return inf
            if r == row - 1:
                return matrix[r][c]
            if (r, c) in memo:
                return memo[(r, c)]
            
            memo[(r, c)] = min(matrix[r][c] + dp(r + 1, c - 1), matrix[r][c] + dp(r + 1, c), matrix[r][c] + dp(r + 1, c + 1))
         
            return memo[(r, c)]
        
        minn = float("inf")
        for i in range(row):
            minn = min(dp(0, i), minn)
            
        return minn