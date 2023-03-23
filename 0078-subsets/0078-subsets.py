class Solution:
    def helper(self, nums, index, curr):
        if index == len(nums):
            self.res.append(curr[:])
            return
        self.helper(nums, index + 1, curr)
        curr.append(nums[index])
        self.helper(nums, index + 1, curr)
        curr.pop()
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.helper(nums, 0, [])
        return self.res