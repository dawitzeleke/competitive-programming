class Solution(object):
    def minSubArrayLen(self, target, nums):
        min_nums= float("inf")
        n= len(nums)
        l=0
        total= 0
        for r in range(n):
            total+= nums[r]
            while total>=target :
                min_nums= min(r-l+1, min_nums)
                total-= nums[l]
                l+=1
            
        return 0 if min_nums== float("inf") else min_nums
