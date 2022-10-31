class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        sortednum= sorted(nums)
        result=[]
        dic= {}
        for i in range (len(sortednum)):
            if sortednum[i] not in dic:
                dic[sortednum[i]]= i
        for i in nums:
            result.append(dic[i])
            
        return result    
