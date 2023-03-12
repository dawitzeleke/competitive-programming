class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        l=[]
        c=0
        for i in range(len(nums)-1):
            if(nums[i]==nums[i+1]):
                nums[i]=nums[i]*2
                nums[i+1]=0
        for i in nums:
            if i!=0:
                l.append(i)
            else:
                c+=1
        return l+[0]*c