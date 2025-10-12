class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = (10 ** 9) + 7

        memo = {}
        
        def helper(curr_sum, remaining):
            if remaining == 0:
                if curr_sum == target:
                    return 1
                return 0

            if curr_sum > target:
                return 0
            if (remaining, curr_sum) in memo:
                return memo[(remaining, curr_sum)]

            total = 0
            for i in range(1, k + 1):
                total += helper(curr_sum + i, remaining - 1)

            memo[(remaining, curr_sum)] = total
            return total
        
        
        return helper(0, n) % MOD

            