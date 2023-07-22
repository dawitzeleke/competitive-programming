class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        up = 1
        down = 1
        
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] < 0:
                down = up + 1
            elif nums[i] - nums[i - 1] > 0:
                up = down + 1
                
        return max(up, down)
            