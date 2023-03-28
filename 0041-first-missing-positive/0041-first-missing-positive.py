class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        for i in range (len(nums)):
             while nums[i] - 1 != i :
                
                if nums[i] >= len(nums) or nums[i] < 0:
                    break
                else:
                    temp = nums[i]-1
                    if nums[i] == nums[nums[i]- 1]:    
                        break
                    nums[i], nums[temp] = nums[temp], nums[i] 
                
                    
        answer = 0
        
        for i in range(len(nums)):
            if nums[i] > 0:
                answer += 1
                if answer != nums[i]:
                    return answer
        return answer + 1
       