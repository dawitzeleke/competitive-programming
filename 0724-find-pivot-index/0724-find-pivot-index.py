class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum1 = 0
        for num in nums:
            sum1 += num
            
        rightsum = sum1
        leftsum = 0
        
        for i in range(len(nums)):
            rightsum -= nums[i]
            if rightsum == leftsum:
                return i
            else:
                leftsum += nums[i]
        
        return -1
                