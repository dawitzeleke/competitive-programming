class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo = defaultdict(int)
        def dp(r, c):  
            if (r, c) in memo:
                return memo[(r, c)]
            if r == len(triangle):
                return 0
            
            sum1 = triangle[r][c] + dp(r + 1, c)
            sum2 = triangle[r][c] + dp(r + 1, c + 1)
            
            memo[(r,c)] = min(sum1, sum2)
            return min(sum1, sum2)
        
        return dp(0, 0)