class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        memo = {}
        
        def dp(i):
            if i in memo:
                return memo[i]
            if i >= len(questions):
                return 0
            if i not in memo:
                memo[i] = max(questions[i][0] + dp(i + questions[i][1] + 1), dp(i + 1))
            
            return memo[i]
            
        return dp(0)