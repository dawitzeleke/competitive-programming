class Solution(object):
    
    def checkArithmeticSubarrays(self, nums, l, r):
        result = []
        for index in range(len(l)):
            result.append(self.checkArithmetic(nums[l[index]: r[index]+1]))
        return result
    
    def checkArithmetic(self, nums):
        nums.sort()
        for index in range(2, len(nums)):
            if nums[index] - nums[index-1]  == nums[index-1] - nums[index-2]:
                continue
            else:
                return False
        return True
