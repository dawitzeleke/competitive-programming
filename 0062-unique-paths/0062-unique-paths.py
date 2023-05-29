class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {(m - 1, n - 1): 1}
        row = m
        col = n
        for r in range( row - 1, -1, -1):
            for c in range( col - 1, -1, -1):
                
                if 0 <= r + 1 <= row - 1 and 0 <= c + 1 <= col - 1:
                    memo[(r, c)] = memo[(r + 1, c)] + memo[r, c + 1]
                elif 0 <= r + 1 <= row - 1:
                    memo[(r, c)] = memo[(r + 1, c)] 
                elif 0 <= c + 1 <= col - 1:
                     memo[(r, c)] = memo[r, c + 1]
                        
                        
        return memo[(0,0)]