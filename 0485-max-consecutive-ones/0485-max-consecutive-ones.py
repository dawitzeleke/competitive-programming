class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxx = float("-inf")
        current_max = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                current_max += 1
                maxx = max(current_max, maxx)
            else:
                current_max = 0
        return maxx if maxx != float("-inf") else 0