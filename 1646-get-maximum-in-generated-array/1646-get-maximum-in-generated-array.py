class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        memo = [0, 1]
        if n < 2:
            return n
        for i in range(2, n + 1):
            if i % 2 == 0:
                memo.append(memo[i // 2])
                
            else:
                memo.append(memo[i // 2] + memo[(i // 2) + 1])
                
        return max(memo)