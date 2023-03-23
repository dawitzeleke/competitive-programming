class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        for i in range (len(nums)):

            while nums[i] - 1 != i and nums[i] != 0:
                temp = nums[i]-1
                nums[i], nums[temp] = nums[temp], nums[i]

        return nums.index(0) + 1 if 0 in nums else 0
