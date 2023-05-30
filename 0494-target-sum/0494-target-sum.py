class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        
        def dp(index, summ):
            if index >= len(nums):
                if summ == target:
                    return 1
                
                return 0
            if not (index, summ) in memo:
                memo[(index, summ)] = dp(index + 1, summ + nums[index]) + dp( index + 1, summ - nums[index])
                                                                                
            return memo[(index, summ)]
                                                                                
        return dp(0, 0)                                                                        