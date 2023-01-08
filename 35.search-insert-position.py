#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        
        if target in nums:
            return nums.index(target)
        else:    
            num1= max(nums)
            if num1< target:
                return len(nums)
            else:
                for i in range(len(nums)):
                    if nums[i]> target:
                        return i
# @lc code=end

