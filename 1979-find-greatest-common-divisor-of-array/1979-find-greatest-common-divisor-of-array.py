class Solution:
    def findGCD(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        
        a = min(nums)
        b = max(nums)
        divisor = 0
        print(a)
        for i in range(a, 0,-1):
            if a % i == 0 and b % i == 0:
                divisor = i
                break
        return divisor
        
        
        