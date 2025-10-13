class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[0 for _ in range(n)] for _ in range(m)]

        print(memo)
        memo[0][0] = 1
        print(memo)
        for r in range(m):
            for c in range(n):
                if (r, c) == (0, 0):
                    continue
                left = 0

                if (c - 1) >= 0:
                    left += memo[r][c - 1]

                top = 0

                if (r - 1) >= 0:
                    top += memo[r - 1][c]

                memo[r][c] = top + left

        return memo[m - 1][n - 1] 