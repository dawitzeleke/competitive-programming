class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        minn = 0
        curr_sum = 0
        for i in nums:
            curr_sum += i
            if curr_sum <= minn:
                minn = curr_sum
        return -minn + 1