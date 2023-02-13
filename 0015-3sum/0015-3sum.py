class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i, n in enumerate (nums):
            if i > 0 and n == nums[i-1]:
                continue
            l = i+1
            r = len(nums)-1
            while r>l:
                if nums[i] + nums[l] + nums[r] == 0: 
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l<r:
                        l += 1
                elif nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                else:
                    l +=1
                    
        return res