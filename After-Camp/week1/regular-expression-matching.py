class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False
            
            temp = i < len(s) and (s[i] == p[j] or p[j] == ".")
            if j + 1 < len(p) and p[j + 1] == "*":
                memo[(i, j)] = dp(i, j + 2) or (temp and dp(i + 1, j))
                return memo[(i, j)]

            if temp:
                memo[(i, j)] = dp(i + 1, j + 1)
                return memo[(i, j)]
            memo[(i, j)] = False
            return memo[(i, j)]
        return dp(0, 0)