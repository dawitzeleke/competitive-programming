class Solution(object):
    def maxOperations(self, nums, k):
        nums.sort()
        counter = 0
        l= 0 
        r = len(nums)-1
        while l<r:
            if nums[l]+ nums[r] == k:
                counter += 1
                l+= 1
                r-= 1
            elif  nums[l]+ nums[r] < k:
                l+=1
            else:
                r-=1

        return counter
