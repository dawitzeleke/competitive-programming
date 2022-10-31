class Solution(object):
    def targetIndices(self, nums, target):
    
        sortednums= sorted(nums)
        target_index=[]
        n= len(sortednums)
        for i in range (n):
            if sortednums[i]==target:
                target_index.append(i)
        return target_index        
                
