class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        n= len(nums)
        counter=[0]*n
        for i in range (n):
            for j in range(n):
                if nums[i]> nums[j]:
                    counter[i]+=1
        return counter   
