class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:

        m = k
        multiplier = 1
        while True:
            temp = m * multiplier
            if temp not in nums:
                return temp

            multiplier += 1
        


