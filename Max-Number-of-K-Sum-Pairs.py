class Solution(object):
    def maxOperations(self, nums, k):
        max_operations=0
        for i in range (len(nums)):
            for j in range(i, len(nums)):
                if nums[i]+nums[j]==k:
                    max_operations+=1
        return max_operations
