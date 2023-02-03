class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        
        count = 0
        l = nums[0]
        for i in range(1, len(nums)):
            r = nums[i]
            if r <= l:
                count += l-r + 1
                r = l + 1 
            l= r
        return count