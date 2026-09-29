class Solution:
    def hasValidPath(self, A: List[List[str]]) -> bool:
        m, n = len(A), len(A[0])

        if ~(m + n) & 1 or A[0][0] == ")" or A[-1][-1] == "(":
            return False

        dp = [0] * (n + 1)
        dp[1] = 1

        for i in range(m):
            for j in range(n):
                dp[j + 1] = ((dp[j + 1] | dp[j]) << 1) >> ((A[i][j] == ')') << 1)

        return bool(dp[n] & 1)