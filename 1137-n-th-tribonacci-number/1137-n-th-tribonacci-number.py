class Solution:
    def tribonacci(self, n: int) -> int:
        memo = collections.defaultdict(int)
        
        def fn(n):
            if n <= 0:
                return 0
            if n == 2 or n == 1:
                return 1
            if not memo[n]:
                memo[n] = fn(n - 3) + fn(n - 2) + fn(n - 1)
                
            return memo[n]
       
        return fn(n)