class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        memo = {}
        n = len(nums)
        for i in range(n):
            
            for j in range(i + 1, n):
                memo[j, nums[j] - nums[i]] = memo.get((i, nums[j] - nums[i]), 1) + 1   
                    
        return max(memo.values())