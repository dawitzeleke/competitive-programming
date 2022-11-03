class Solution(object):
    def minPairSum(self, nums):
        nums=sorted(nums)
        i=0
        j=len(nums)-1
        answer=0
        while i<j:
            answer=max(answer,nums[i]+nums[j])
            i+=1
            j-=1
        
        return answer
