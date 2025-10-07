class Solution:
    def soupServings(self, n: int) -> float:

        memo = defaultdict(int)

        def dp(a, b):
            if a <= 0 and b <= 0:
                return 0.5

            if a <= 0:
                return 1

            if b <= 0:
                return 0
            if (a, b) in memo:
                return memo[(a, b)]
            curr_pro = dp(a - 100, b) + dp(a - 75, b - 25) + dp(a - 50, b - 50) + dp(a - 25, b - 75)

            memo[(a, b)] = curr_pro / 4
            return curr_pro / 4

        return dp(n, n)