class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        
        def dp(temp):
             
            if temp in memo:
                return memo[temp]
            
            if temp < 0:
                return inf
           
            elif temp == 0:
                return 0
            else:
                minn = min( 1 + dp(temp - c) for c in coins)
                memo[temp] = minn
            
            return memo[temp]
        
        fewestCoin = dp(amount) 
        
        if fewestCoin != inf:
            return fewestCoin
        else:
            return -1