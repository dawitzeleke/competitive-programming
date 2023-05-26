class Solution:
    def climbStairs(self, m: int) -> int:
        memo = defaultdict(int)
        def fn(n):
            if n > m:
                return 0
            if n == m:  
                return 1
            if not memo[n + 1] and not memo[n + 2]:
                memo[n] = fn(n + 2) + fn(n + 1)
 
            elif not memo[n + 1] and memo[n + 2]:
                memo[n] = memo[n + 2] + fn(n + 1) 
    
            elif not memo[n + 2] and memo[n + 1]:
                memo[n] = memo[n + 1] + fn(n + 2)
            else:
                  memo[n] = memo[n + 1] + memo[n + 2]
            return memo[n]
        fn(0)
        return memo[0]