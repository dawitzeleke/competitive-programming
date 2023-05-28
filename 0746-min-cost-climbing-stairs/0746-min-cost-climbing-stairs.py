class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = collections.defaultdict(int)
        def dp(n):
            if n >= len(cost):
                return 0
            if n == len(cost) - 1:
                return cost[-1]
            
            if not memo[n]:
                memo[n] = min( dp(n + 1) + cost[n], dp(n + 2) + cost[n])
                
            return memo[n]
        
        
        return min( dp(0), dp(1))