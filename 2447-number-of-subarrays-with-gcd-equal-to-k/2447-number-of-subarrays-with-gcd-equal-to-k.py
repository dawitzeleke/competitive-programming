class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        counter = 0
        
        for i in range(len(nums)):
            tempGCD = 0
            for j in range(i, len(nums)):
                tempGCD = gcd(tempGCD, nums[j])
                
                if tempGCD == k:
                    counter += 1
                    
                    
        return counter
        