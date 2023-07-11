class Solution:
    def numDecodings(self, s: str) -> int:
        
        memo = defaultdict(int)
        
        def dp(i):
            if i in memo:
                return memo[i]
            
            if i == len(s):
                return 1
            if s[i] == "0":
                return 0
            
            single = dp(i + 1)
            
            double = 0
            
            if i + 2 <= len(s) and 1 <= int(s[i: i + 2]) <= 26:
                double += dp(i + 2)
                
            memo[i] = single + double
            
            return memo[i]
        
        
        return dp(0)