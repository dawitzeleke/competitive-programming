class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums) <= 4:
            return 0
        currentmax = float("inf")
        left = 3
        right = len(nums) - 1
        
        while left >= 0:
            
            currentmax = min(currentmax, nums[right] - nums[left])
            right -= 1
            left -= 1
        
        return currentmax