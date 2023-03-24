class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for i in range (len(nums)):
            
            while nums[i] != i + 1 and nums[i] != -1 :
                if nums[i] == nums[nums[i]- 1]:
                    res.append(nums[i])  
                    nums[i] = -1
                else:
                     nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1] 
                
        return res