class Solution:
    def maxSum(self, nums: list[int], k: int, mul: int) -> int:
        n = len(nums)
        temp = sorted(nums, reverse=True)[:k]

        max_sum = 0 
        m = mul
        for num in temp:
            if m > 0:
                max_sum += num * m
                m -= 1
            else:
                max_sum += num

        return max_sum