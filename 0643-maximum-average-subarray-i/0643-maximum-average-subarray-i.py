class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) < 2:
            return nums[0]
        _sum = 0
        for i in range(k):
            _sum += nums[i]
        l = 0
        r = k
        curr_sum = _sum
        max_ave = _sum / k
        while r < len(nums):
            curr_sum -= nums[l]
            curr_sum += nums[r]
            max_ave = max(max_ave, curr_sum/k)
            l += 1
            r += 1
            
        return max_ave