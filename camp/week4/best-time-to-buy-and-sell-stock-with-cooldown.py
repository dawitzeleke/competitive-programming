class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        
        def dp(i, state):
            if i >= len(prices):
                return 0
            if (i, state) in memo:
                return memo[(i, state)]
            
            cooldown = dp(i + 1, state)
            if state:
                buying = dp(i + 1, not state) - prices[i]
                memo[(i, state)] = max(buying, cooldown)
                
            else:
                selling = dp(i + 2, not state) + prices[i]
                memo[(i, state)] = max(selling, cooldown)
                
            return memo[(i, state)]
        
        
        return dp(0, True)