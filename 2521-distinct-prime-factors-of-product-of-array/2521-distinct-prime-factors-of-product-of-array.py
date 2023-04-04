class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        def trial_division_simple(n: int) -> list[int]:
            factorization: list[int] = []
            d = 2

            while d * d <= n:
                while n % d == 0:
                    factorization.append(d)
                    n //= d
                d += 1
            if n > 1:
                factorization.append(n)

            return factorization
        
        res = set()
        
        for num in nums:

            temp = set(trial_division_simple(num))
            
            res = res.union(temp)
        
        return len(res)