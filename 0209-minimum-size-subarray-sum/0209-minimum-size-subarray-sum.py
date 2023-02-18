class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        r = 0
        summ = 0
        m_l = len(nums)
        res = False
        while r<len(nums):
            summ += nums[r]
            if summ < target:
                r += 1
            else:
                res = True
                m_l = min(m_l, r-l+1)
                while summ > target and l < r:
                    summ -= nums[l]
                    l += 1
                    if summ >= target:
                        m_l = min(m_l, r-l+1)
                r += 1
        if res:
            return m_l
        else:
            return 0
       