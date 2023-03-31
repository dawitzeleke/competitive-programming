class Solution:
    
    def helper(self, current, nums):
        if len(current) == len(self.nums):
            self.ans.append(current[:])
        for num in self.nums:
            if num not in current:
                current.append(num)
                self.helper(current, nums)
                current.pop()
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        self.nums = nums
        self.helper([], nums)
        return self.ans