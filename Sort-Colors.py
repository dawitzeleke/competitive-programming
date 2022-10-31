class Solution:
    def sortColors(self, nums):
        left= 0 
        curr = 0 
        right = len(nums)-1 
        
        while curr <= right:
            if nums[curr] == 0:
                nums[left],nums[curr]= nums[curr],nums[left]
                left += 1 
                curr += 1  
                
            elif nums[curr] == 2:
                nums[curr],nums[right]  = nums[right],nums[curr] 
                right -= 1 
                
            else:
                curr += 1 
