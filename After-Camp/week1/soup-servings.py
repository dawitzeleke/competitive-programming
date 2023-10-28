class Solution:
    def soupServings(self, n: int) -> float:
        if n >= 4450:
            return 1
        memo = {}
        def dp(A, B):
            if (A, B) in memo:
                return memo[(A, B)]
            if A <= 0 and B <= 0:
                return 0.5
            if A <= 0:
                return 1
            if B <= 0:
                return 0

            memo[(A, B)] = 0.25 * (dp(A - 100, B) + dp(A - 75, B - 25) + dp(A - 50, B - 50) + dp(A - 25, B - 75))
            return memo[(A, B)]

        return dp(n, n)