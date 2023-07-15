class Solution:
    def rob(self, nums: List[int]) -> int:
        
        return max(nums[0], self.dp(nums[1:]), self.dp(nums[:-1]))
    def dp(self, arr):
        robbery1, robbery2 = 0, 0
        for num in arr:
            temp = max(num + robbery1, robbery2)
            robbery1 = robbery2
            robbery2 = temp


        return robbery2