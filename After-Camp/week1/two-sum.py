class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        
        for i in range (len(nums)):
            comp = target - nums[i]
            if comp in h:
                return [i, h[comp]]
            else: 
                h[nums[i]] = i
                